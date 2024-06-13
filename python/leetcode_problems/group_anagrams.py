# 49. Group Anagrams - Leetcode medium
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


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # create empty dictionary
        num_dict = {}

        # loop through the array of strings 
        for i in range(len(strs)):
            
            # sort each string, then join back together using join and sorted function.
                # sort each string, using the sorted function, then join back together.
            sorted_word = ''.join(sorted(strs[i]))
            
            
            # check if the sorted string is a key within the dictionary
                # if not, then create an empty list
                # if does exist, just append that word into the list of that sorted corresponding word. 
            if sorted_word not in num_dict:
                num_dict[sorted_word] = []

            num_dict[sorted_word].append(strs[i])


        # after the finished iterating through the strs list
            # get list of all the values(arrays) in num_dict dictionary, using num_dict.values()
            # iterate through that list, and append it to the empty solution array that will be returned as the final solution array.
        # create an empty array
        sol_array = []
        for array in num_dict.values():
            sol_array.append(array)

        return sol_array



    

