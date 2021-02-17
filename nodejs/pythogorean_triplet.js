// Node.js Essentials : Pythogorean triplet

// For a Pythagorean triplet where a + b + c = 1000, find the product of abc.

var a = 1;
var b = 2;
var c = Math.sqrt(a*a + b*b);
var sum = a+b+c;
while(sum != 1000){
    if(sum > 1000){
        a++;
        b = a+1;
    } else {
        b++;
    }
    c = Math.sqrt(a*a + b*b);
    sum = a + b + c;
}

console.log('a:' + a + '  b:' + b + '  c:' + c);
console.log(a*b*c);