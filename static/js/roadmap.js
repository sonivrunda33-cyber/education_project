document.addEventListener("DOMContentLoaded", () => {

    // Animate roadmap cards
    const items = document.querySelectorAll(".timeline-item");

    items.forEach((item, index) => {

        item.style.opacity = "0";
        item.style.transform = "translateX(-25px)";

        setTimeout(() => {

            item.style.transition = "all 0.6s ease";

            item.style.opacity = "1";

            item.style.transform = "translateX(0)";

        }, index * 150);

    });


    // Animate progress bars
    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach((bar) => {

        const progress =
            bar.dataset.progress || "0";

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width =
                Math.min(
                    100,
                    Math.max(0, Number(progress))
                ) + "%";

        }, 400);

    });

});