# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.

# TESTS
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# First attempt
# create a dictionary
    # store each unique number as a key
        # for value, store number of occurences of that key.



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}

        for i in range(len(nums)):
                        
            print(nums[i])
            if nums[i] not in num_dict.keys():
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1

    

