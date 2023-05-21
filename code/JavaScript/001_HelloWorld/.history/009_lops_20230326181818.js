for (i = 0; i < 10; i++){
    console.log(i);
}

let arr = [1, 2, "a", 4];

for (item in arr) {
    console.log(arr[item]);
}

let person = { fname: "John", lname: "Doe", age: 25 };

for (let x in person) {
  console.log(x +" =>  "+person[x])
}


let arr1 = ["X","Y","Z"];

for (item of arr1) {
    console.log(item);
}


const map = new Map();
map.set("k1", "v1");
map.set("k2", "v2");

console.log(map.get("k1"));

console.log(map);

const set = new Set();
set.add("v1");
set.add("v2");
console.log(set);
