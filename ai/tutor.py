def tutor_reply(message):

    text = message.lower().strip()

    if "loop" in text:

        return (
            "Loops repeat a block of code. "
            "In Python, common loops are for and while.\n\n"
            "Example:\n"
            "for i in range(5):\n"
            "    print(i)"
        )

    if "function" in text:

        return (
            "A function is a reusable block of code.\n\n"
            "Example:\n"
            "def add(a, b):\n"
            "    return a + b"
        )

    if "oop" in text or "class" in text:

        return (
            "OOP means Object Oriented Programming. "
            "Important concepts include Class, Object, "
            "Inheritance, Encapsulation and Polymorphism."
        )

    if "python" in text:

        return (
            "Python is a high-level programming language "
            "known for its simple syntax and large ecosystem."
        )

    if "hello" in text or "hi" in text:

        return (
            "Hey! 👋 I'm SkillTwin AI Tutor. "
            "Ask me about Python, loops, functions, OOP "
            "or programming problems."
        )

    return (
        "I can help you with Python, loops, functions, "
        "OOP and problem solving. Try asking me a specific "
        "question."
    )