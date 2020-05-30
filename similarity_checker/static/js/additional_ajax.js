$(document).ready(function () {
    $("#loginForm").on('submit', function (e) { 
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
                        $("#errorLogin").html(err);
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

    $("#registerForm").on('submit', function (e) { 
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
                        $("#errorRegister").html(err);
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

    $("#check1_btn").on('click', function () {
        var url = window.origin + "/check1"
        var urlSave = window.origin + "/saveSessionTable1"
        var tableResult = ""

        $.ajax({
            type: "POST",
            url: url,
            success: function (response) {
                if (response['status'] === "failed") {
                    function showError() {
                        var err = "<span class=\"text-danger\">"+response['error']+"</span"
                        $("#errorCheck1").html(err);
                    }
                    
                    showError()
                } else {
                    $("#check1_result").css('display', 'block');

                    if ($("#save1_btn").css('display') == 'none') {
                        $("#save1_btn").css('display', '');
                    }

                    var err = ""
                    $("#errorCheck1").html(err);

                    var thead = "<thead class=\"thead-light\"><tr><th class=\"text-center\"><span>Suspect Document</span></th><th class=\"text-center\"><span>Document Name</span></th><th class=\"text-center\"><span>Percentage</span></th></tr></thead>"
                    var trOpen = "<tr>"
                    var tdRowspan = "<td rowspan=\""
                    var tdRowspanCon = "\" style=\"text-align: center;\">"
                    var tdOpen = "<td>"
                    var tdClose = "</td>"
                    var spanOpen = "<span>"
                    var spanClose = "</span>"
                    var divProgress = "<div class=\"progress\">"
                    var divProgressDanger = "<div class=\"progress-bar bg-danger\" style=\"width:"
                    var divProgressSafe = "<div class=\"progress-bar bg-success\" style=\"width:"
                    var divProgressWarning = "<div class=\"progress-bar bg-warning\" style=\"width:"
                    var divProgressClose = "%;\">"
                    var divAccClose = "%</div>"
                    var divClose = "</div>"
                    var trClose = "</tr>"

                    var simResult = response['result']

                    for (docName in simResult) {
                        var suspectName = docName
                        var finDetail = ""
                        var rowCount = simResult[docName].length + 1

                        for (i in simResult[docName]) {
                            var tempDetail = ""
                            var documentName = simResult[docName][i][0]
                            var accuracy = Math.round(simResult[docName][i][1])

                            if (accuracy <= 60) {
                                if (accuracy <= 0) {
                                    accuracy = 0
                                }

                                tempDetail = trOpen + tdOpen + spanOpen + documentName + spanClose + tdClose + tdOpen + divProgress + divProgressSafe + accuracy + divProgressClose + accuracy + divAccClose + divClose + tdClose + trClose
                            } else if (accuracy > 60 && accuracy <= 85) {
                                tempDetail = trOpen + tdOpen + spanOpen + documentName + spanClose + tdClose + tdOpen + divProgress + divProgressWarning + accuracy + divProgressClose + accuracy + divAccClose + divClose + tdClose + trClose
                            } else if (accuracy > 85) {
                                tempDetail = trOpen + tdOpen + spanOpen + documentName + spanClose + tdClose + tdOpen + divProgress + divProgressDanger + accuracy + divProgressClose + accuracy + divAccClose + divClose + tdClose + trClose
                            }
                            
                            finDetail = finDetail + tempDetail
                        }
                        var finalStr = trOpen + tdRowspan + rowCount + tdRowspanCon + spanOpen + suspectName + spanClose + tdClose + trClose + finDetail
                        tableResult = tableResult+finalStr
                    }

                    function showResult() {
                        $("#check1_tbody").html(tableResult);
                    }

                    showResult()
                    
                    var tableJson = "{"
                    + "\"header\":" + JSON.stringify(thead) + ","
                    + "\"data\":" + JSON.stringify(tableResult)
                    + "}";

                    $.ajax({
                        type: "POST",
                        url: urlSave,
                        data: tableJson,
                        dataType: "json",
                        success: function (response) {
                            console.log(response)
                        }
                    });
                }
            }
        });
    });

    $("#check2_btn").on('click', function () {
        var url = window.origin + "/check2"
        var urlSave = window.origin + "/saveSessionTable2"

        $.ajax({
            type: "POST",
            url: url,
            success: function (response) {
                if (response['status'] === "failed") {
                    function showError() {
                        var err = "<span class=\"text-danger\">"+response['error']+"</span"
                        $("#errorCheck2").html(err);
                    }
                    
                    showError()
                } else {
                    $("#check2_result").css('display', 'block');

                    if ($("#save2_btn").css('display') == 'none') {
                        $("#save2_btn").css('display', '');
                    }

                    var err = ""
                    $("#errorCheck2").html(err);

                    var tableResult = ""

                    var thead = "<thead class=\"thead-light\"><tr><th class=\"text-center\"><span>Suspect Document</span></th><th class=\"text-center\"><span>Source Document</span></th><th class=\"text-center\"><span>Percentage</span></th></tr></thead>"
                    var trOpen = "<tr>"
                    var tdRowspan = "<td rowspan=\""
                    var tdRowspanCon = "\" style=\"text-align: center;\">"
                    var tdOpen = "<td>"
                    var tdClose = "</td>"
                    var spanOpen = "<span>"
                    var spanClose = "</span>"
                    var divProgress = "<div class=\"progress\">"
                    var divProgressDanger = "<div class=\"progress-bar bg-danger\" style=\"width:"
                    var divProgressSafe = "<div class=\"progress-bar bg-success\" style=\"width:"
                    var divProgressWarning = "<div class=\"progress-bar bg-warning\" style=\"width:"
                    var divProgressClose = "%;\">"
                    var divAccClose = "%</div>"
                    var divClose = "</div>"
                    var trClose = "</tr>"

                    var simResult = response['result']

                    for (docName in simResult) {
                        var suspectName = docName
                        var finDetail = ""
                        var rowCount = simResult[docName].length + 1

                        for (i in simResult[docName]) {
                            var tempDetail = ""
                            var documentName = simResult[docName][i][0]
                            var accuracy = Math.round(simResult[docName][i][1])

                            if (accuracy <= 60) {
                                if (accuracy <= 0) {
                                    accuracy = 0
                                }

                                tempDetail = trOpen + tdOpen + spanOpen + documentName + spanClose + tdClose + tdOpen + divProgress + divProgressSafe + accuracy + divProgressClose + accuracy + divAccClose + divClose + tdClose + trClose
                            } else if (accuracy > 60 && accuracy <= 85) {
                                tempDetail = trOpen + tdOpen + spanOpen + documentName + spanClose + tdClose + tdOpen + divProgress + divProgressWarning + accuracy + divProgressClose + accuracy + divAccClose + divClose + tdClose + trClose
                            } else if (accuracy > 85) {
                                tempDetail = trOpen + tdOpen + spanOpen + documentName + spanClose + tdClose + tdOpen + divProgress + divProgressDanger + accuracy + divProgressClose + accuracy + divAccClose + divClose + tdClose + trClose
                            }
                            
                            finDetail = finDetail + tempDetail
                        }
                        var finalStr = trOpen + tdRowspan + rowCount + tdRowspanCon + spanOpen + suspectName + spanClose + tdClose + trClose + finDetail
                        tableResult = tableResult+finalStr
                    }

                    function showResult() {
                        $("#check2_tbody").html(tableResult);
                    }

                    showResult()

                    var tableJson = "{"
                    + "\"header\":" + JSON.stringify(thead) + ","
                    + "\"data\":" + JSON.stringify(tableResult)
                    + "}";

                    $.ajax({
                        type: "POST",
                        url: urlSave,
                        data: tableJson,
                        dataType: "json",
                        success: function (response) {
                            console.log(response)
                        }
                    });
                }
            }
        });
    });

    function exportToPdf(tableName) {
        html2canvas(document.getElementById(tableName), {
            onrendered: function (canvas) {
                var data = canvas.toDataURL();
                var docDefinition = {
                    content: [{
                        image: data,
                        width: 500
                    }]
                };
                pdfMake.createPdf(docDefinition).download("Table.pdf");
            }
        });
    }

    $("#export1_btn").on('click', function() {
        exportToPdf('check1_table')
    });

    $("#export2_btn").on('click', function() {
        exportToPdf('check2_table')
    });

    $("#save1_btn").on('click', function () {
        var url = window.origin + "/saveTable1ToDb"

        $.ajax({
            type: "POST",
            url: url,
            success: function (response) {
                console.log(response)
                $("#save1_btn").css('display', 'none');
            }
        });
    });

    $("#save2_btn").on('click', function () {
        var url = window.origin + "/saveTable2ToDb"

        $.ajax({
            type: "POST",
            url: url,
            success: function (response) {
                console.log(response)
                $("#save2_btn").css('display', 'none');
            }
        });
    });

    function deleteDetailBtn(idx) {
        var url = window.origin + "/delete"
        var data = "{"
        + "\"id\":" + idx
        + "}"

        $.ajax({
            type: "POST",
            url: url,
            data: data,
            dataType: "json",
            success: function (response) {
                console.log(response)}});
    }

    function generateScript(idx) {
        var scriptOpen = "<script>"
        var scriptClose = "</script>" 
        var a = "$(document).ready(function () {$(\"#export_btn"+ idx +"\").on('click', function(){ exportToPdf(\"nama_tabel"+ idx +"\")}); $(\"#deleteDetail_btn"+ idx +"\").on('click', function(){ deleteDetailBtn("+ idx +")}); });"

        return scriptOpen + a + scriptClose
    }

    $("#history_tab").on('click', function () {
        var url = window.origin + "/getHistory"

        var divRow = "<div class=\"row\">"
        var divCol = "<div classs=\"col\">"
        var divFloatR = "<div class=\"float-right\">"
        var divAccordion = "<div class=\"panel-group\" id=\"accordion\">"
        var divPanel = "<div class=\"panel panel-default\">"
        var divPanelHead = "<div class=\"panel-heading\">"
        var divOpenId = "<div id=\""
        var divCloseId = "\" class=\"panel-collapse collapse in\">"
        var divPanelBody = "<div class=\"panel-body\">"
        var divClose = "</div>"
        var h3PanelTitle = "<h4 class=\"panel-title\">"
        var h3Close = "</h4>"
        var aCollapse = "<a data-toggle=\"collapse\" class=\"text-dark text-decoration-none\" data-parent=\"#accordion\" href=\"#"
        var aCollapseClose = "\">"
        var aClose = "</a>"
        var tableOpen = "<table class=\"table table-hover\" id=\"nama_tabel"
        var tClose = "\">"
        var tableClose = "</table>"

        var btnExportOpen = "<button class=\"btn btn-success\" id=\"export_btn"
        var btnExportMid = "\" onclick=\"exportToPdf('nama_tabel"
        var btnExportClose = "')\"><span class=\"fa fa-file-download mr-1\"></span><span>Export as PDF</span></button>"

        var btnDeleteOpen = "<button class=\"btn bg-danger\" id=\"deleteDetail_btn"
        var btnDeleteMid = "\" onclick=\"deleteDetailBtn("
        var btnDeleteClose = ")\"><span class=\"fa fa-exclamation mr-1\" style=\"color: white;\"></span><span class=\"text-white\">Delete History</span></button>"

        var index = 0

        $.ajax({
            type: "POST",
            url: url,
            success: function (response) {
                console.log(response)
                if (response['status'] === "failed") {
                    
                } else {
                    var finTemp = ""
                    var temp = ""
                    var header = ""
                    var detail = ""
                    var tempDetail = ""

                    for (getDate in response['result']) {
                        header = divPanel
                        + divPanelHead 
                        + h3PanelTitle 
                        + aCollapse
                        + "collapse" + index
                        + aCollapseClose
                        + getDate
                        + aClose
                        + h3Close
                        + divClose
                        + divClose
                        + '<br>'

                        for (i in response['result'][getDate]) {
                            var btn = divRow
                            + divCol
                            + divFloatR
                            + btnExportOpen
                            + i
                            + btnExportMid
                            + i
                            + btnExportClose
                            + btnDeleteOpen
                            + i
                            + btnDeleteMid
                            + i
                            + btnDeleteClose
                            + divClose
                            + divClose
                            + divClose

                            tempDetail = tempDetail
                            + tableOpen
                            + i
                            + tClose
                            + response['result'][getDate][i]
                            + tableClose
                            + '<br>'
                        }

                        detail = divOpenId
                        + "collapse" + index
                        + divCloseId
                        + divPanelBody
                        + tempDetail
                        + divClose
                        + divClose

                        temp = temp + header + detail
                        index = index+1
                    }
                    
                    finTemp = divAccordion + temp + divClose

                    function setHistoryData() {
                        $("#history_sect").html(finTemp);
                    }

                    setHistoryData()
                }
            }
        });
    });
});