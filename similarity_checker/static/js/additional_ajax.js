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

        var url = window.origin + "/auth/login"

        $.ajax({
            type: "POST",
            global: false,
            async: true,
            url: url,
            data: jsonData,
            dataType: "json",
            contentType: "application/json",
            success: function (response) {
                if (response['status'] == "failed") {
                    function showError() {
                        var err = "<span class=\"text-danger\">"+response['error']+"</span"
                        $("#errorLogin").append(err);
                    }

                    showError()
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

        var url = window.origin + "/auth/register"

        $.ajax({
            type: "POST",
            url: url,
            data: jsonData,
            dataType: "json",
            contentType: "application/json",
            success: function (response) {
                if (response['status'] == "failed") {
                    function showError() {
                        var err = "<span class=\"text-danger\">"+response['error']+"</span"
                        $("#errorRegister").append(err);
                    }

                    showError()
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