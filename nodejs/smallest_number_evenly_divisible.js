// Node.js Essentials : Evenly divisible number

// What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

function smallestDivisible(limit) {
    var i, n = 1;

    function largestPower(n, limit) {
        var p, e = 2, largest = n;
        while ((p = Math.pow(n, e)) <= limit) {
            largest = p;
            e += 1;
        }
        return largest;
    }

    function isPrime(n) {
    var sq = Math.sqrt(n);
    for (var i=2; i<=sq; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}


    for (i = 3; i <= limit; i += 2) {
        if (isPrime(i)) {
            n *= largestPower(i, limit);
        }
    }

    return n * largestPower(2, limit);
}

console.log(smallestDivisible(20));