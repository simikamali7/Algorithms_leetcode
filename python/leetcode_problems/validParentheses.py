# 20. Valid Parentheses

# use a stack --> used to match up
#  O(n) - time
#  O(n) - memory

# use hashMap to map out closing and opening parentheses
# SELF IS ALWAYS INCLUDED IN THE PARAMETERS LIST
# s is a string that passed into the function isValid
#  isValid returns a bool value

class Solution:
    def isValid(self, s: str ) -> bool:
        stack = []
        
        # hashMap that maps out the closing to the opening brace
        # easier/better to set closers as the keys, and opening as vals
        closeToOpen= {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        # loop through each character in the string
            # check if char is in closeToOpen --> checking the key
                # if the stack is not empty and the the last item in the list(item in the top of stack) == the value that key (c) maps to, pop it off the stack.
                # else return false, if either condition is false for that c
            # if c is not among the keys(closing braces), then it is an opening bracket, so add it to the stack with append.

            # after the string is finished iterated, if the stack is empty (null), return True
            # if stack is not empty, return false --> not valid parentheses.

        for c in s:
            if c in closeToOpen:
                # make sure that stack isn't empty
                # and make sure item at top of stack is the opening 
                # brace to the closing brace 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # getting an open parentheses in the string
            # append it to the stack.
            else:
                stack.append(c)
        
        # if the stack is empty (null), return True
        # if stack is not empty, return false 
        if not stack:
            return True
        else:
            return False
                
    
                