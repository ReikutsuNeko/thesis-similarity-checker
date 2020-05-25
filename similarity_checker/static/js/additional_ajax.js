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

        var jsonData = "{"
        + "\"email\"" + ":\"" + data["emailLogin"] + "\","
        + "\"password\"" + ":\"" + data["passwordLogin"] + "\""
        + "}"

        $.ajax({
            type: "POST",
            global: false,
            async: true,
            url: "http://127.0.0.1:5000/auth/login",
            data: jsonData,
            dataType: "json",
            contentType: "application/json",
            success: function (response) {
                if (response['status'] == "failed") {
                    alert(response['error'])
                } else {
                    window.location.reload()
                }
            },
            error: function(status, statusText) {
                console.log(statusText)
            }
        });
    });

    $("#registerForm").submit(function (e) { 
        e.preventDefault();
        
        var form_info = $(this).serializeArray()
        var data = {}

        for (var key in form_info) {
            var k = form_info[key]["name"];
            var v = form_info[key]["value"];
            data[k] = v;
        }

        var jsonData = "{"
        + "\"name\"" + ":\"" + data["nameRegister"] + "\"" + ","
        + "\"email\"" + ":\"" + data["emailRegister"] + "\"" + ","
        + "\"password\"" + ":\"" + data["passwordRegister"] + "\"" + ","
        + "\"passwordConfirmation\"" + ":\"" + data["passwordConfirmation"] + "\""
        + "}";

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/auth/register",
            data: jsonData,
            dataType: "json",
            contentType: "application/json",
            success: function (response) {
                if (response['status'] == "failed") {
                    alert(response['error'])
                } else {
                    window.location.reload()
                }
            },
            error: function(status, statusText) {
                console.log(statusText)
            }
        });
    });
});