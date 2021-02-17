// Node.js Essentials: Working with Timers


// interval

function intervalFunc(arg) {
console.log('TCS');
}

setInterval(intervalFunc, 5000);


// timeout

function myFunc(arg) {
console.log('TCS');
}

setTimeout(myFunc, 2000);


// interval + timeout 
function myFunc(arg) {
console.log('TCS');
}

setInterval(myFunc, 2000);
clearInterval(10000);
