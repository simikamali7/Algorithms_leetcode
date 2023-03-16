/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    indices = [];    
    var num1;
    var num2; 

    for(let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if(nums[i] + nums[j] == target) {
                indices.push(j);
                indices.push(i);
            } 
        }
    }
    return indices;

};

// second method: use a set, and subtract each number in array from the target, and see if the remainder value exists. 9-4 = 5 --> see if 5 exists.
    // res = []
	// sums = set()

	// for val in arr:
	// 	if target - val in sums:
	// 		res.append([val, target - val])
	// 	sums.add(val)
	// return res