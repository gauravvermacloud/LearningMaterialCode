async function myFn(name){
    var millisecondsToWait = 10000;
    setTimeout(function() {
        // Whatever you want to do after the wait
    }, millisecondsToWait);
    if (name !== "GV") {
        return "Hello " + name;
    }
    {
        Q.reject("Incorrect Name")
    }
}

myFn("GV").then(
    function (value) { console.log(value); },
    function (error) { console.log(error); }
);

myFn("AV").then(
    (value) => console.log(value),
    (error) => console.log(error)
);