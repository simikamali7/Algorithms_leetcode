/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    return x == x.toString().split('').reverse().join('');
    console.log(x);
};

// methodology:
// stringify x, then split for each character, then reverse all the characters, and then join all back into 1 string. 
// then compare it to x;   
    // returns true if x palindrome as palindrome is the same word spelt the same backward as front. 