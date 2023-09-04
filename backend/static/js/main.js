var prevScrollPos = window.pageYOffset;

window.addEventListener("scroll", function() {
    var currentScrollPos = window.pageYOffset;
    var navContainer = document.querySelector(".nav_container");

    if (prevScrollPos > currentScrollPos) {
        // Scrolling up, bring the navigation bar down
        navContainer.classList.remove("nav-tucked-up");
        navContainer.classList.add("nav-come-down");
    } else {
        // Scrolling down, tuck the navigation bar up
        navContainer.classList.remove("nav-come-down");
        navContainer.classList.add("nav-tucked-up");
    }

    prevScrollPos = currentScrollPos;
});