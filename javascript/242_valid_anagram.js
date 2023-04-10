
// find whether 2 strings are valid anagrams

// method: split the strings into array of characters, sort these arrays, and join them back.
    // if they are ==, then it must be an anagram. 

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    splittedt = t.split('')
    splitteds = s.split('')

    console.log(splittedt.sort())
    console.log(splitteds.sort())

    if(splittedt.sort().join('') == splitteds.sort().join('')) {
        return true;
    }
    return false;
};


// other method using ASCII codes - making a table