from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import json

from utils.database import (
    get_db,
    init_db
)

from ai.weakness_detector import (
    analyze_performance
)

from ai.quiz_generator import (
    generate_quiz
)

from ai.recommendation import (
    build_roadmap
)

from ai.tutor import (
    tutor_reply
)


app = Flask(__name__)

app.secret_key = "skilltwin-ai-secret-key"

init_db()


# ---------------- HOME ----------------

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ---------------- SIGNUP ----------------

@app.route(
    "/signup",
    methods=["GET", "POST"]
)
def signup():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:

            return "Please fill all fields."

        db = get_db()

        existing = db.execute(
            "SELECT id FROM users WHERE email=?",
            (email,)
        ).fetchone()

        if existing:

            db.close()

            return "Email already registered."

        db.execute(
            """
            INSERT INTO users
            (name,email,password_hash,role)

            VALUES (?,?,?,?)
            """,

            (
                name,
                email,
                generate_password_hash(password),
                "student"
            )
        )

        db.commit()
        db.close()

        return redirect(
            url_for("login")
        )

    return render_template(
        "login.html"
    )


# ---------------- LOGIN ----------------

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()

        user = db.execute(
            """
            SELECT *
            FROM users
            WHERE email=?
            """,
            (email,)
        ).fetchone()

        db.close()

        if user and check_password_hash(
            user["password_hash"],
            password
        ):

            session["user_id"] = user["id"]
            session["name"] = user["name"]
            session["role"] = user["role"]

            if user["role"] == "admin":

                return redirect(
                    url_for("admin")
                )

            return redirect(
                url_for("dashboard")
            )

        return render_template(
            "login.html",
            error="Invalid email or password."
        )

    return render_template(
        "login.html"
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("index")
    )


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    db = get_db()

    result = db.execute(
        """
        SELECT *
        FROM assessment_results
        WHERE user_id=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (session["user_id"],)
    ).fetchone()

    db.close()

    data = None

    if result:

        data = {
            "score": result["score"],
            "strengths": json.loads(
                result["strengths"] or "[]"
            ),
            "weaknesses": json.loads(
                result["weaknesses"] or "[]"
            ),
            "analysis": json.loads(
                result["analysis_json"] or "{}"
            )
        }

    return render_template(
        "dashboard.html",
        name=session.get("name"),
        result=data
    )


# ---------------- ASSESSMENT ----------------

@app.route(
    "/assessment",
    methods=["GET", "POST"]
)
def assessment():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        data = request.get_json()

        answers = data.get(
            "answers",
            []
        )

        analysis = analyze_performance(
            answers
        )

        db = get_db()

        db.execute(
            """
            INSERT INTO assessment_results
            (
                user_id,
                score,
                strengths,
                weaknesses,
                analysis_json
            )

            VALUES (?,?,?,?,?)
            """,

            (
                session["user_id"],
                analysis["overall"],
                json.dumps(
                    analysis["strengths"]
                ),
                json.dumps(
                    analysis["weaknesses"]
                ),
                json.dumps(
                    analysis
                )
            )
        )

        for skill, score in analysis[
            "skills"
        ].items():

            db.execute(
                """
                INSERT INTO student_progress
                (
                    user_id,
                    skill,
                    score
                )

                VALUES (?,?,?)

                ON CONFLICT(user_id,skill)

                DO UPDATE SET
                score=excluded.score
                """,

                (
                    session["user_id"],
                    skill,
                    score
                )
            )

        db.commit()
        db.close()

        return jsonify(
            analysis
        )

    return render_template(
        "assessment.html"
    )


# ---------------- ROADMAP ----------------

@app.route("/roadmap")
def roadmap():

    if "user_id" not in session:
        return redirect(url_for("login"))

    db = get_db()

    progress = db.execute(
        """
        SELECT skill, score
        FROM student_progress
        WHERE user_id=?
        ORDER BY score ASC
        """,
        (session["user_id"],)
    ).fetchall()

    db.close()

    # Convert database rows into dictionary
    skills = {}

    for row in progress:
        skills[row["skill"]] = row["score"]

    # Generate personalized roadmap
    roadmap_data = build_roadmap(skills)

    return render_template(
        "roadmap.html",
        roadmap=roadmap_data,
        skills=skills,
        name=session.get("name")
    )

# ---------------- QUIZ ----------------

@app.route(
    "/quiz",
    methods=["GET", "POST"]
)
def quiz():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        data = request.get_json()

        topic = data.get(
            "topic",
            "Python"
        )

        return jsonify(
            generate_quiz(topic)
        )

    return render_template(
        "quiz.html"
    )


# ---------------- TUTOR ----------------

@app.route(
    "/tutor",
    methods=["GET", "POST"]
)
def tutor():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        data = request.get_json()

        message = data.get(
            "message",
            ""
        )

        return jsonify({
            "reply": tutor_reply(
                message
            )
        })

    return render_template(
        "tutor.html"
    )


# ---------------- ADMIN ----------------

@app.route("/admin")
def admin():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    if session.get("role") != "admin":

        return "Access denied", 403

    db = get_db()

    users = db.execute(
        """
        SELECT id,name,email,role,created_at
        FROM users
        ORDER BY id DESC
        """
    ).fetchall()

    assessments = db.execute(
        """
        SELECT
        COUNT(*) AS total,
        AVG(score) AS average
        FROM assessment_results
        """
    ).fetchone()

    db.close()

    return render_template(
        "admin.html",
        users=users,
        total_assessments=assessments["total"],
        average_score=round(
            assessments["average"] or 0
        )
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )