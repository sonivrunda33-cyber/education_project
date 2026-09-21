document.addEventListener(
    "DOMContentLoaded",
    () => {

        const buttons =
            document.querySelectorAll(".btn");

        buttons.forEach(button => {

            button.addEventListener(
                "click",
                () => {

                    button.style.transform =
                        "scale(.97)";

                    setTimeout(() => {

                        button.style.transform =
                            "";

                    }, 120);

                }
            );

        });

    }
);