# 2 sum in python

# brute force solution:
    # loop through the list, and start a second loop 1 index after the 1 first index, and keep comparing the 2 index i, j,
    # if add to the target, return,
        # else, keep iterating.

# more space efficient that solution 2, but much slower.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j




# more efficient solution

# use a dictionary for more efficieny - O(1) average time complexity. 
# while loop -> while target - num[1] not in checked
    # add in the nums[i] as a key in the dictionary along with its index as the value. 
    # increment the index 1.

# when loop doesn't run, return the key '2' in the dictionary and i.
    # eg; checked[target("9")-nums[i]("7") == 2, i("1")]
            # so returning checked[2], 1) 
                # the key 2 in checked as a value of 0, so returning the value 0.
                # so returning 0, 1 --> which is 2, 7 ==> which adds to 9.

# much more time efficient, but less space efficient

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        i = 0
        while target - nums[i] not in checked:
            checked[nums[i]] = i
            i += 1

        return [checked[target - nums[i]], i]


