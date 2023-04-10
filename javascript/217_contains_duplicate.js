// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// method = create a set --> sets cannot contain duplicates
// loop through the array and check if the set already contains that same number using .has() --> return true;
    // if doesn't add into set
    // else, return false after loop entire array.

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var set = new Set()
    for (var i =0; i<nums.length; i++){
        if(set.has(nums[i])){
            return true;
        }
        set.add(nums[i]);
    }
    return false;
};

// 