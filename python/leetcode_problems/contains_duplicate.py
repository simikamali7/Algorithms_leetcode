# LEETCODE 217 - CONTAINS DUPLICATE.


# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


# TEST DATA:
    # Example 1:

    # Input: nums = [1,2,3,1]
    # Output: true
    # Example 2:

    # Input: nums = [1,2,3,4]
    # Output: false
    # Example 3:

    # Input: nums = [1,1,1,3,3,4,3,2,4,2]
    # Output: true





# main solution/method:
    # use sets --> sets cannot contain duplicates.

    # create an empty set.
    # loop through the nums list
        # for each element, check if it exists in the set.
            # if exists, return true as output
        # if condition doesn't pass = not in the set, 
            # add the element to the set.

        # keep looping through list.

    # if none of the elements are duplicates, then return false as output.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()

        for i in range(len(nums)):
            if nums[i] in duplicate_set:
                return True
            duplicate_set.add(nums[i])
        return False