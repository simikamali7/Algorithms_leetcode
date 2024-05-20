# 1299. Replace Elements With Greatest Element On Right Side

# given an array arr, replace every element in that array
#  with the greatest element among the elements to its right,
# and replace the last element with -1.

# input arr = [17,18,5,4,6,1]
#  output arr = []


# doing a lot of repeated work/calculations when going through
    # keep on getting the max value of everything to right.

    # need to iterate through in reverse order


# went in reverse order --> gives o(n) time
#initial max = -1 ==> b/c the last value will always be negative
        # reverse iteration
        # newMax = max(oldmax, arr[i])
            # newMax will be the maximum between the oldMax and the
            # previous position i in the array.
                # b/c the max 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        # going backwards
        for i in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr

arr = [1,4,2,21,256]

print(min(arr)) 