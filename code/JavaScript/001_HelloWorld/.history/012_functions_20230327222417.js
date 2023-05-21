'option strict'

function add(a, b) {
    return a + b;
}

function log() {
    console.log("message");
}


const diff = function difference(a, b) {
    return a - b;    
}


mux = function (a, b) {
    return a * b;
}

console.log(add(2, 3));
log();

console.log(diff(2, 3));

console.log(mux(2, 3));

const div = (a, b) => { return a / b; }

console.log(div(7, 2));


const obj = {};
obj.add = add;

console.log(obj.add(2, 3));

const obj1 = { f: diff };
console.log(obj1.f(2, 3));


const z = function fx(d = '2') {//specify default value
    console.log(d);
}

z('hello');
z();





//called immediately
(function fx () {
        console.log("called");
});

(function fx1 (a,b) {
        console.log(a+b);
})(1, 2);



//calling an annonymous function

let f = function (z) {
    z;
}

f(
    function  () {
        console.log('hello world');
    }
);


f(
    function (a, b) {
        console.log(a * b);
    }(2, 3)
);


f(
    function  fx1() {
        console.log('hello world');
    }
);


f(
    function fx2(a, b) {
        console.log(a * b);
    }(2, 3)
);


ar = () => { console.log('hello'); }

ar();

ar2 = (a, b) => { return a + b; }
ar2(2, 3);

ar3 = (a, b) => a + b;
ar3(2,3)
