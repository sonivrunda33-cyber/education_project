QUIZZES = {

    "Python": [
        {
            "question": "Which keyword is used to define a function?",
            "options": [
                "func",
                "define",
                "def",
                "function"
            ],
            "answer": 2
        },
        {
            "question": "Which data type stores True or False?",
            "options": [
                "int",
                "bool",
                "str",
                "float"
            ],
            "answer": 1
        },
        {
            "question": "Which symbol is used for comments?",
            "options": [
                "//",
                "/*",
                "#",
                "<!--"
            ],
            "answer": 2
        },
        {
            "question": "Which function displays output?",
            "options": [
                "display()",
                "print()",
                "show()",
                "output()"
            ],
            "answer": 1
        },
        {
            "question": "Which collection is ordered and changeable?",
            "options": [
                "tuple",
                "set",
                "list",
                "string"
            ],
            "answer": 2
        }
    ],

    "OOP": [
        {
            "question": "What does OOP stand for?",
            "options": [
                "Object Oriented Programming",
                "Object Operating Program",
                "Open Object Programming",
                "Only Object Program"
            ],
            "answer": 0
        },
        {
            "question": "Which keyword creates a class in Python?",
            "options": [
                "object",
                "class",
                "struct",
                "new"
            ],
            "answer": 1
        },
        {
            "question": "Which concept hides implementation details?",
            "options": [
                "Inheritance",
                "Encapsulation",
                "Looping",
                "Iteration"
            ],
            "answer": 1
        },
        {
            "question": "Which concept allows a child class to use parent features?",
            "options": [
                "Inheritance",
                "Encapsulation",
                "Compilation",
                "Iteration"
            ],
            "answer": 0
        },
        {
            "question": "What is an instance of a class called?",
            "options": [
                "Variable",
                "Object",
                "Method",
                "Package"
            ],
            "answer": 1
        }
    ]
}


def generate_quiz(topic="Python"):

    return QUIZZES.get(
        topic,
        QUIZZES["Python"]
    )