// Node.js Essentials : Working with callback functions


// Find the sum of all the multiples of 3 and 5, below and including 1000.

function solution(number) {
  let sum = 0;
  for (let i = 3; i < number; i++) {
    if ((i % 3 === 0) || (i % 5 === 0)) {
      sum += i;
    }
  }
  return sum;
}

console.log(solution(1000))