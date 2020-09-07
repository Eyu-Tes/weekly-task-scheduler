$(document).ready(function() {
    // remove the active class from previously active menu item 
    $(".nav li a").removeClass("active");
    // set the active class to the current menu item
    $('a[href="' + this.location.pathname + '"]').addClass('active');
    // make slider menu visible 
    document.querySelector('#slider').classList.remove('invisible');
});
