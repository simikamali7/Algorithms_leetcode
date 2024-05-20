# liner time algorithm with no extra space.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # need a left and a right pointer --> l starts at 0, r starts at the end
        l,r = 0, len(numbers) - 1

        # left pointer will never be greater than right pointer.
        while l < r:
            curSum = numbers[l] + numbers[r]

            # if current sum is greater than target, need to shift right pointer back 1.
            if curSum > target:
                r -=1
            # if sum is too small, shift l pointer 1 more to right
            elif curSum < target:
                l += 1
            
            # if the sum == target, return l and r pointers
            # based on 1, so add 1 to each
            else:
                return [l +1, r + 1]


