$(document).ready(function () {
    $("#loginForm").submit(function (e) { 
        e.preventDefault();
    
        var form_info = $(this).serializeArray();
        var data = {};
    
        for (var key in form_info) {
            var k = form_info[key]["name"];
            var v = form_info[key]["value"];
            data[k] = v;
        }

        console.log(data)
    
        $.ajax({
            type: "POST",
            url: "127.0.0.1:5000/auth/login",
            data: data,
            dataType: "json",
            beforeSent: function (){
                console.log("WOY")
            },
            success: function (response) {
                console.log(response);
            }
        });
    });
});