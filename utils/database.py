import sqlite3

from config.config import DATABASE_PATH
from werkzeug.security import generate_password_hash


def get_db():
    db = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row
    return db


def init_db():

    db = get_db()

    # ---------------- USERS TABLE ----------------

    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'student',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ---------------- ASSESSMENT RESULTS ----------------

    db.execute("""
        CREATE TABLE IF NOT EXISTS assessment_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            strengths TEXT,
            weaknesses TEXT,
            analysis_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ---------------- STUDENT PROGRESS ----------------

    db.execute("""
        CREATE TABLE IF NOT EXISTS student_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            skill TEXT NOT NULL,
            score INTEGER NOT NULL,
            UNIQUE(user_id, skill),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ---------------- ROADMAP ----------------

    db.execute("""
        CREATE TABLE IF NOT EXISTS roadmaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ---------------- DEMO ADMIN ----------------

    admin = db.execute(
        "SELECT id FROM users WHERE email=?",
        ("admin@skilltwin.ai",)
    ).fetchone()

    if not admin:

        db.execute(
            """
            INSERT INTO users
            (name, email, password_hash, role)
            VALUES (?, ?, ?, ?)
            """,
            (
                "SkillTwin Admin",
                "admin@skilltwin.ai",
                generate_password_hash("admin123"),
                "admin"
            )
        )

    # ---------------- DEMO STUDENT ----------------

    student = db.execute(
        "SELECT id FROM users WHERE email=?",
        ("student@example.com",)
    ).fetchone()

    if not student:

        db.execute(
            """
            INSERT INTO users
            (name, email, password_hash, role)
            VALUES (?, ?, ?, ?)
            """,
            (
                "Demo Student",
                "student@example.com",
                generate_password_hash("student123"),
                "student"
            )
        )

    db.commit()
    db.close()