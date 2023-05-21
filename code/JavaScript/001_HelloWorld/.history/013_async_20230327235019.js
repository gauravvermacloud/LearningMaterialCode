async function myFn(){
    var millisecondsToWait = 5000;
    setTimeout(function() {
        // Whatever you want to do after the wait
    }, millisecondsToWait);

    return "Hello World";
}

myFn().then(
    function (value) { console.log(value); },
    function (error) { console.log(error); }
);