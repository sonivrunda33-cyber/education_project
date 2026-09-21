document.addEventListener("DOMContentLoaded", () => {

    const cards =
        document.querySelectorAll(".glass-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform =
            "translateY(20px)";

        setTimeout(() => {

            card.style.transition =
                "all .7s ease";

            card.style.opacity = "1";

            card.style.transform =
                "translateY(0)";

        }, index * 80);

    });


    const orb =
        document.querySelector(".orb");

    if (orb) {

        document.addEventListener(
            "mousemove",
            (event) => {

                const x =
                    (event.clientX /
                    window.innerWidth - .5) * 20;

                const y =
                    (event.clientY /
                    window.innerHeight - .5) * 20;

                orb.style.transform =
                    `translate(${x}px, ${y}px)`;

            }
        );

    }

});