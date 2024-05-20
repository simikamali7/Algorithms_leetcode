# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub


# Neetcode solutuion

#53. Maximum Subarray
# easy 
    
# given an integer array, find the contiguous subarray (containing at least one number)
# which has the larest sum and return its sum. 
    
# example
    # input [-2,-1,-3,4,-1,2,1,-5,4]
    # output = 6 
    # exaplanation = [4,-1, 2, 1] has the largest sum of 6

# sliding window solution?
    

# O(n) solution
        # get rid of all negative prefix numbers 
        # sliding window like solution 

class solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # need to keep track of the largest subArray
        maxSub = nums[0] 

        # need to be tracking the current sum
        curSum = 0

        # iterate through the num array.
        for n in nums:
            # if there is negative prefix, we need to remove it.
                # if current sum is ever less than 0, reset it. 
            if curSum < 0:
                curSum = 0
            # then add n 
            curSum += n
            # curSum, can be greater than the current maxSub, so check it after every addition to curSub.
            maxSub = max(maxSub, curSum)

        # after going through entire nums array, return the maxSub array.
        return maxSub


