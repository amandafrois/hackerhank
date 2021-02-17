// Node.js Essentials : Sum of squares

// Find the difference between the sum of the squares of the first hundred natural numbers, and the square of the sum.

const sumSquareDiff = (n) => {
  const numbers = [...Array(n + 1).keys()];
  const sumOfSquares = numbers.reduce((accumulator, number) => accumulator + (number ** 2));
  const squareOfSum = numbers.reduce((accumulator, number) => accumulator + number) ** 2;
  return squareOfSum - sumOfSquares;
}
console.log(sumSquareDiff(100));