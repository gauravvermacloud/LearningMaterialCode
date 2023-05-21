async myFn(){
    var millisecondsToWait = 500;
    setTimeout(function() {
        // Whatever you want to do after the wait
    }, millisecondsToWait);

    return "Hello World";
}

myFn().then(
    function (value) { console.log(value); }
);