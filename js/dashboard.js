document.addEventListener("DOMContentLoaded", () => {

    // Animate progress bars
    const progressBars =
        document.querySelectorAll(".progress-bar");

    progressBars.forEach((bar) => {

        const targetWidth =
            bar.style.width;

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width =
                targetWidth;

        }, 300);

    });


    // Animate stat numbers
    const stats =
        document.querySelectorAll(
            ".stat-card strong"
        );

    stats.forEach((stat) => {

        const text =
            stat.textContent.trim();

        const match =
            text.match(/\d+/);

        if (!match) return;

        const target =
            parseInt(match[0]);

        const suffix =
            text.includes("%")
                ? "%"
                : "";

        let current = 0;

        const duration = 1000;

        const steps = 40;

        const increment =
            target / steps;

        const interval =
            duration / steps;

        stat.textContent =
            "0" + suffix;

        const counter =
            setInterval(() => {

                current += increment;

                if (current >= target) {

                    current = target;

                    clearInterval(counter);
                }

                stat.textContent =
                    Math.round(current) +
                    suffix;

            }, interval);

    });


    // Dashboard cards entrance animation
    const cards =
        document.querySelectorAll(
            ".dashboard-grid .glass-card, .stats-grid .glass-card"
        );

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform =
            "translateY(20px)";

        setTimeout(() => {

            card.style.transition =
                "all 0.6s ease";

            card.style.opacity = "1";

            card.style.transform =
                "translateY(0)";

        }, index * 120);

    });


    // Add hover glow effect
    cards.forEach((card) => {

        card.addEventListener(
            "mousemove",
            (event) => {

                const rect =
                    card.getBoundingClientRect();

                const x =
                    event.clientX -
                    rect.left;

                const y =
                    event.clientY -
                    rect.top;

                card.style.background = `
                    radial-gradient(
                        circle at ${x}px ${y}px,
                        rgba(139,92,246,0.15),
                        rgba(255,255,255,0.03)
                    )
                `;

            }
        );


        card.addEventListener(
            "mouseleave",
            () => {

                card.style.background =
                    "";

            }
        );

    });

});