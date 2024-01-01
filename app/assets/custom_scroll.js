window.onscroll = function() {
    var navbar = document.getElementById('scroll-comp');
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        navbar.style.color = 'rgba(255, 255, 255, 0)';
    } else {
        navbar.style.color = 'rgba(255, 255, 255, 1)';
    }
};
