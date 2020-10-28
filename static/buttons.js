$(document).ready(function() {

    var row_one = $("#lessons").clone();
    var row_two = $("#break").clone();
    var above = $("#toptop").clone();

    $("#Lbtn").click(function() {
        (row_one).clone().appendTo("#lessontable");
    });

    $("#Bbtn").click(function() {
        (row_two).clone().appendTo("#lessontable");
    });

    $("#Dbtn").click(function() {
        $("#lessontable tr:last").remove();
    });

});