const input =
    document.getElementById(
        "messageInput"
    );

const sendBtn =
    document.getElementById(
        "sendBtn"
    );

const messages =
    document.getElementById(
        "chatMessages"
    );


function addMessage(
    text,
    type
) {

    const message =
        document.createElement(
            "div"
        );

    message.className =
        `message ${type}`;


    message.innerHTML = `

        <div class="avatar">
            ${type === "ai" ? "🤖" : "👤"}
        </div>

        <div class="message-content">
            ${text}
        </div>

    `;


    messages.appendChild(
        message
    );


    messages.scrollTop =
        messages.scrollHeight;
}


async function sendMessage() {

    const text =
        input.value.trim();


    if (!text) {
        return;
    }


    addMessage(
        text,
        "user"
    );


    input.value = "";


    addMessage(
        "Thinking...",
        "ai"
    );


    const thinking =
        messages.lastElementChild;


    try {

        const response =
            await fetch(
                "/tutor",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: text
                    })
                }
            );


        const data =
            await response.json();


        thinking.remove();


        addMessage(
            data.reply,
            "ai"
        );

    }

    catch (error) {

        thinking.remove();

        addMessage(
            "Something went wrong. Please try again.",
            "ai"
        );

    }

}


sendBtn.addEventListener(
    "click",
    sendMessage
);


input.addEventListener(
    "keydown",
    event => {

        if (
            event.key === "Enter"
        ) {

            sendMessage();

        }

    }
);