document.addEventListener('DOMContentLoaded', () => {
    // FAQ Accordion
    document.querySelectorAll('.faq-question').forEach(button => {
        button.addEventListener('click', () => {
            const currentlyActive = document.querySelector('.faq-question.active');
            const answer = button.nextElementSibling;
            
            if (currentlyActive && currentlyActive !== button) {
                currentlyActive.classList.remove('active');
                currentlyActive.nextElementSibling.style.display = 'none';
            }
            
            const isActive = button.classList.toggle('active');
            answer.style.display = isActive ? 'block' : 'none';
        });
    });

    // Mobile Menu
    const burger = document.getElementById("burger");
    const closeBtn = document.getElementById("close");
    const mobileMenu = document.getElementById("mobileMenu");

    if (burger && closeBtn && mobileMenu) {
        window.toggleMenu = function(open) {
            if (open) {
                burger.classList.add("hide");
                closeBtn.classList.add("show");
                mobileMenu.classList.add("open");
                document.body.classList.add("mobile-open");
            } else {
                burger.classList.remove("hide");
                closeBtn.classList.remove("show");
                mobileMenu.classList.remove("open");
                document.body.classList.remove("mobile-open");
            }
        };

        burger.onclick = () => toggleMenu(true);
        closeBtn.onclick = () => toggleMenu(false);

        window.addEventListener("resize", () => {
            if (window.innerWidth > 1400) {
                toggleMenu(false);
            }
        });
    }
});
