// Node.js Essentials : nth prime

// What is the 1001th prime number?


function is_prime(num) {
    var sq = Math.sqrt(num);
    for (var i=2; i<=sq; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

    function getBigPrime () {
    var holder = 0;
    var counter = 1;
        for (var p=3; counter<=10000; p+=2) { 
            if (is_prime(p)){ 
                holder = p 
                counter += 1; // should be inside the if
            }
        }
        console.log(holder);
    }

    getBigPrime();