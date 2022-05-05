window.addEventListener('load', function() {
    var problems = Array.from(document.getElementsByClassName("problem"));
    problems.forEach(function(problem) {
        var eval = problem.childNodes.item(3).value;
        var ival = problem.childNodes.item(5).value;
        var enode = document.getElementById("expect");
        var inode = document.getElementById("input");
        var text = document.getElementById(problem.childNodes.item(1).id);
        console.log(text);console.log(problem);
        problem.addEventListener("click", function() {
            text.style.color="#0000cd"
            enode.innerHTML = eval;
            inode.innerHTML = ival;
        }, false);
    });
});
