// Node.js Essentials : Lasrgest prime factor

// What is the largest prime factor of the number 600851475143? 

var divisor = 2;
var number = 600851475143;

while(number > 1){
    if(number % divisor === 0){
        number /= divisor;
    } else {
        divisor++;
    }
}

console.log(divisor);