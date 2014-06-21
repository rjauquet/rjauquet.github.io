$(function() {
    $('#container').isotope({
        itemSelector: '.icon',
        layoutMode: 'fitRows'
    });
});

$("#toggle-shown").click(function (){
    $("#navigation").toggle();
    $("#toggle-shown").toggleClass("toggle-show");
    $("#toggle-shown").toggleClass("toggle-hide");
});
