// 問題表示（イベント）
window.addEventListener('load', function() {
    var button = document.getElementById("button-area").childNodes;
    console.log(button)
    var titles = Array.from(document.getElementsByClassName("title"));

    titles.forEach(function(title) {
        title.childNodes.forEach(function(detale) {
            console.log(title.childNodes);
            if(detale.nodeName == "DETAILS") {
                console.log("DETAILS");
                console.log(detale.childNodes);
                detale.childNodes.forEach(function(problems) {
                    if(problems.className == "problems") {
                        console.log("problems");
                        console.log(problems.childNodes);
                        problems.childNodes.forEach(function(problem) {
                            if(problem.className == "problem") {
                                console.log("problem");
                                console.log(problem.childNodes)
                                var childNodes = problem.childNodes
                                var id = problems.childNodes.item(1).id
                                var eval = childNodes.item(3).value;
                                var ival = childNodes.item(5).value;
                                var sval = childNodes.item(7).value;
                                var enode = document.getElementById("expect");
                                var inode = document.getElementById("input");
                                
                                var text = childNodes.item(1)

                                childNodes.item(1).addEventListener("click", function() {
                                    text.style.color="#0000cd"
                                    enode.innerHTML = eval;
                                    inode.innerHTML = ival;
                                    button.item(3).setAttribute('value', id);
                                    button.item(5).setAttribute('value', ival);
                                    button.item(7).setAttribute('value', eval);
                                    button.item(9).setAttribute('value', sval);
                                }, false);
                            }
                        })   
                    }
                });
            }
        });
    });
});
