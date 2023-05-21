for (i = 0; i < 10; i++){
    console.log(i);
}

const arr = [1, 2, "a", 4];

for (item in arr) {
    console.log(arr[item]);
}

const person = { fname: "John", lname: "Doe", age: 25 };

for (let x in person) {
  console.log(x +" =>  "+person[x])
}