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
    


# attempt 2:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # iterate through the list
        for i in range(len(nums)):
            current_num = i
            current_count = 0 
            if i+1 != current_num: 
                return current_num
            else: 
                current_count += 1
        # keep track of the number of each item 
        # compare the sizes of the most frequent
        # return


# Neetcode solution 
# use bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary
        count = {}

        # make a list of lists, where the list is size of nums 
        freq = [[] for i in range(len(nums)+ 1)]

        # iterate through nums array, add in occurence into dictionary.
        # dictionary keys = each unique number
            # count.get(n, 0) --> grabs the value of the key "n", and if not exists, returns 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # for each key:value in count "count.items":
            # go to that index in the frequency list of lists, and add n. 
        for n, c in count.items():
            freq[c].append(n)
        

        res = []
    
        # loop through the list of lists backwards, from last item to first. ((freq) - 1, 0, -1) --> means from the last index to 0, last argument is the step argument.
        # for each index in the frequency list, add in that number into the results list to return.
        # if the length of the results list == k --> stop the loop b/c found the top k element.

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res





