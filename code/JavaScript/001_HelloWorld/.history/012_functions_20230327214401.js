function add(a, b) {
    return a + b;
}

function log() {
    console.log("message");
}


diff = function difference(a, b) {
    return a - b;    
}


mux = function (a, b) {
    return a * b;
}

console.log(add(2, 3));
log();

console.log(diff(2, 3));

console.log(mux(2, 3));

div = (a, b) => { return a / b; }

console.log(div(7, 2));


obj = {};
obj.add = add;

console.log(o.add(2, 3));

