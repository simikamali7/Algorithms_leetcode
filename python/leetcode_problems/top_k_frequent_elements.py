#  Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# my first attempt

# create a dictionary that stores each unique number as a key, and its value as the frequency of the number.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}

        for i in range(len(nums)):
                        
            print(nums[i])
            if nums[i] not in num_dict.keys():
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1

        num_vals = num_dict.values()
    
