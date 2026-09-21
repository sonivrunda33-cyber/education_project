QUESTIONS = [
    "python",
    "python",
    "loops",
    "loops",
    "functions",
    "functions",
    "oop",
    "oop",
    "problem_solving",
    "problem_solving"
]


def analyze_performance(answers):

    # Make sure we always have 10 answers
    answers = answers[:10]

    while len(answers) < 10:
        answers.append(1)


    topics = {
        "Python Basics": [],
        "Loops": [],
        "Functions": [],
        "OOP": [],
        "Problem Solving": []
    }


    topic_map = {
        "python": "Python Basics",
        "loops": "Loops",
        "functions": "Functions",
        "oop": "OOP",
        "problem_solving": "Problem Solving"
    }


    # ---------------- COLLECT SCORES ----------------

    for index, answer in enumerate(answers):

        try:
            score = int(answer)
        except (ValueError, TypeError):
            score = 1

        # Keep score between 1 and 10
        score = max(1, min(score, 10))

        question_topic = QUESTIONS[index]

        topic_name = topic_map[
            question_topic
        ]

        topics[topic_name].append(score)


    # ---------------- SKILL SCORES ----------------

    skills = {}

    for topic, scores in topics.items():

        if scores:

            average = sum(scores) / len(scores)

            percentage = round(
                (average / 10) * 100
            )

        else:

            percentage = 0

        skills[topic] = percentage


    # ---------------- OVERALL SCORE ----------------

    if skills:

        overall = round(
            sum(skills.values()) / len(skills)
        )

    else:

        overall = 0


    # ---------------- STRENGTHS ----------------

    strengths = [
        skill
        for skill, score in skills.items()
        if score >= 70
    ]


    # ---------------- WEAKNESSES ----------------

    weaknesses = [
        skill
        for skill, score in skills.items()
        if score < 60
    ]


    # ---------------- RECOMMENDATION ----------------

    if weaknesses:

        weakest_skill = min(
            skills,
            key=skills.get
        )

        recommendation = (
            f"Your main focus should be "
            f"{weakest_skill}. "
            f"Practice this skill regularly "
            f"with examples and small projects."
        )

    elif strengths:

        recommendation = (
            "Your fundamentals are strong. "
            "Now focus on advanced concepts "
            "and practical projects."
        )

    else:

        recommendation = (
            "Complete more assessments "
            "to build your personalized "
            "learning profile."
        )


    # ---------------- FINAL RESULT ----------------

    return {

        "overall": overall,

        "skills": skills,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendation": recommendation
    }