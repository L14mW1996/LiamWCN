// Use camelCase in javascript

function funcExample() { //function decleration
    console.log("hello World");
};

//Variable Decloration

let myName = "Liam" //Let is changeable
var yourName = "You" // Variable is legacy code, not really used
const name = "Name" // Const is unchangeable

function taskHider(){
    let element = document.getElementById("task-box")
    element.classList.toggle("hidden");
}