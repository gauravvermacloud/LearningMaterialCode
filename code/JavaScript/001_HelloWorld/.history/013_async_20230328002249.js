async function myFn(name){
    var millisecondsToWait = 10000;
    setTimeout(function() {
        // Whatever you want to do after the wait
    }, millisecondsToWait);
    throw TypeError("Message")
    return "Hello " + name;


}

myFn("GV").then(
    function (value) { console.log(value); },
    function (error) { console.log(error); }
).catch(
    function (ex) { console.log(ex); }
);

myFn("AV").then(
    (value) => console.log(value),
    (error) => console.log(error)
);