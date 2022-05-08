window.addEventListener('load', function() {
    var btn = document.querySelector("#btn")

    btn.addEventListener('click', function() {
        btn.disabled = true;
        var title = document.querySelector("#title_name").value
        var problem = document.querySelector("#problem_name").value
        var input = document.querySelector("#input_data").value
        var output = document.querySelector("#expect_output_data").value
        if(title == "" || problem == "" || input == "" || output == "") {
            window.alert("空の入力項目があります。");
            btn.disabled = false;
        }else {
            var form = document.querySelector("#form")
            form.action="http://127.0.0.1:5000/problem"
            form.method="post"
            form.submit();
        }
    })
});
