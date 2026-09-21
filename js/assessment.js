const questions = [

    {
        question:
            "How comfortable are you with Python basics?",
        options: [
            "Beginner",
            "I know the basics",
            "Good",
            "Very good"
        ],
        scores: [2, 5, 8, 10]
    },

    {
        question:
            "How well do you understand Python variables?",
        options: [
            "Not at all",
            "A little",
            "Good",
            "Excellent"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "How comfortable are you with loops?",
        options: [
            "Not comfortable",
            "Basic",
            "Good",
            "Excellent"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "Can you solve problems using loops?",
        options: [
            "No",
            "Sometimes",
            "Usually",
            "Yes"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "How well do you understand functions?",
        options: [
            "Not at all",
            "Basic",
            "Good",
            "Excellent"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "Can you create functions independently?",
        options: [
            "No",
            "With help",
            "Mostly",
            "Yes"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "How well do you understand OOP?",
        options: [
            "Not at all",
            "Basic",
            "Good",
            "Excellent"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "Do you understand classes and objects?",
        options: [
            "No",
            "A little",
            "Good",
            "Very well"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "How good are you at problem solving?",
        options: [
            "Beginner",
            "Basic",
            "Good",
            "Advanced"
        ],
        scores: [1, 4, 8, 10]
    },

    {
        question:
            "How confidently can you solve coding problems?",
        options: [
            "Not confident",
            "Sometimes",
            "Usually",
            "Very confident"
        ],
        scores: [1, 4, 8, 10]
    }

];


let currentQuestion = 0;

let answers = [];

let selectedScore = null;


const container =
    document.getElementById(
        "questionContainer"
    );

const nextBtn =
    document.getElementById(
        "nextBtn"
    );


function showQuestion() {

    const q =
        questions[currentQuestion];

    selectedScore = null;

    document.getElementById(
        "questionNumber"
    ).textContent =
        `Question ${currentQuestion + 1} / ${questions.length}`;


    document.getElementById(
        "questionProgress"
    ).style.width =
        `${((currentQuestion + 1) / questions.length) * 100}%`;


    let html = `
        <div class="question-title">
            ${q.question}
        </div>
    `;


    q.options.forEach(
        (option, index) => {

            html += `
                <button
                    class="option"
                    data-score="${q.scores[index]}">
                    ${option}
                </button>
            `;

        }
    );


    container.innerHTML = html;


    document
        .querySelectorAll(".option")
        .forEach(option => {

            option.addEventListener(
                "click",
                () => {

                    document
                        .querySelectorAll(".option")
                        .forEach(o =>
                            o.classList.remove(
                                "selected"
                            )
                        );

                    option.classList.add(
                        "selected"
                    );

                    selectedScore =
                        Number(
                            option.dataset.score
                        );

                }
            );

        });

}


nextBtn.addEventListener(
    "click",
    async () => {

        if (selectedScore === null) {

            alert(
                "Please select an answer."
            );

            return;
        }


        answers.push(
            selectedScore
        );


        if (
            currentQuestion <
            questions.length - 1
        ) {

            currentQuestion++;

            showQuestion();

            return;
        }


        nextBtn.disabled = true;

        nextBtn.textContent =
            "ANALYZING...";


        const response =
            await fetch(
                "/assessment",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        answers: answers
                    })
                }
            );


        const result =
            await response.json();


        container.classList.add(
            "hidden"
        );

        nextBtn.classList.add(
            "hidden"
        );


        const resultContainer =
            document.getElementById(
                "resultContainer"
            );


        resultContainer.classList.remove(
            "hidden"
        );


        resultContainer.innerHTML = `

            <div class="badge">
                AI ANALYSIS COMPLETE
            </div>

            <h2 style="font-size:45px;margin:20px 0;">
                ${result.overall}%
            </h2>

            <p>
                ${result.recommendation}
            </p>

            <br>

            <h3>
                Strengths
            </h3>

            <p>
                ${
                    result.strengths.length
                    ? result.strengths.join(", ")
                    : "Keep practicing!"
                }
            </p>

            <br>

            <h3>
                Areas to Improve
            </h3>

            <p>
                ${
                    result.weaknesses.length
                    ? result.weaknesses.join(", ")
                    : "No major weaknesses detected."
                }
            </p>

            <br>

            <a
                href="/dashboard"
                class="btn primary">
                VIEW DASHBOARD →
            </a>

        `;

    }
);


showQuestion();