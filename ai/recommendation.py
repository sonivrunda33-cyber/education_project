def build_roadmap(skills):

    if not skills:
        return {
            "title": "Your Personalized Learning Roadmap",
            "steps": [],
            "message": "Complete the assessment first to generate your roadmap."
        }

    # Weakest skill first
    sorted_skills = sorted(
        skills.items(),
        key=lambda item: item[1]
    )

    steps = []

    for index, (skill, score) in enumerate(sorted_skills, start=1):

        if score < 40:
            level = "Beginner"
            action = f"Learn the basic concepts of {skill}."
            tasks = [
                f"Learn {skill} fundamentals",
                f"Solve 5 basic {skill} questions",
                f"Build one small {skill} practice project"
            ]

        elif score < 60:
            level = "Needs Improvement"
            action = f"Strengthen your {skill} fundamentals."
            tasks = [
                f"Revise important {skill} concepts",
                f"Solve 10 practice problems",
                f"Build a small project using {skill}"
            ]

        elif score < 80:
            level = "Intermediate"
            action = f"Improve your {skill} through practical projects."
            tasks = [
                f"Practice intermediate {skill} problems",
                f"Study advanced concepts",
                f"Build a practical {skill} project"
            ]

        else:
            level = "Strong"
            action = f"Keep improving {skill} with advanced challenges."
            tasks = [
                f"Practice advanced {skill}",
                f"Explore real-world use cases",
                f"Build an advanced {skill} project"
            ]

        steps.append({
            "step": index,
            "skill": skill,
            "score": score,
            "level": level,
            "action": action,
            "tasks": tasks,
            "completed": False
        })

    weakest_skill = sorted_skills[0][0]

    return {
        "title": f"Personalized Roadmap",
        "focus": weakest_skill,
        "steps": steps,
        "message": f"Your current priority is {weakest_skill}."
    }


def get_recommendation(skills):

    if not skills:
        return "Complete your assessment to get personalized recommendations."

    weakest_skill, weakest_score = min(
        skills.items(),
        key=lambda item: item[1]
    )

    if weakest_score < 40:
        return (
            f"Start with the basics of {weakest_skill} "
            f"and practice regularly."
        )

    if weakest_score < 60:
        return (
            f"Your {weakest_skill} needs more practice. "
            f"Focus on examples and small projects."
        )

    if weakest_score < 80:
        return (
            f"Your {weakest_skill} foundation is good. "
            f"Move toward intermediate projects."
        )

    return (
        f"You are strong in {weakest_skill}. "
        f"Try advanced challenges."
    )


def get_next_skill(skills):

    if not skills:
        return None

    return min(
        skills.items(),
        key=lambda item: item[1]
    )[0]