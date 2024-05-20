
# MY SOLUTION:

# use a dictionary
    # assign letter to numerical value mapping
    # make a global count 
    # parse the Letters into characters, and add them to the count.
        # insert if statements for special cases for subtraction

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        

# make a case to handle those specific cases:
    # IV = 5
    # IX = 9 

    # XL = 50-10 
    # XC = 100-10

    # CD = 500-100 
    # CM = 1000-100

        # aux variable to hold the sum to be returned
        sum = 0

        # dictionary to map Roman Letters to number values
        letToNum = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # split each string into letters using list function
        splittedLets = list(s)
        
        # loop through the list, but have to use range(len(splittedLets)-1)
        # check for each of the 3 unique cases, if I X or C,
            # then simply subtract that I x or C value from the sum, but make sure I am referencing the dictionary key and not the list.
            # else statement, none of the cases above occured, just add the value based on letter key to sum
        for letter in range(len(splittedLets)-1):
            print(splittedLets[letter])
            if splittedLets[letter] == "I" and (splittedLets[letter+1] == "V" or splittedLets[letter+1] == "X"):
                sum -= letToNum[splittedLets[letter]]
                print(sum)
            elif splittedLets[letter] == "X" and (splittedLets[letter+1] == "L" or splittedLets[letter+1] == "C"):
                sum -= letToNum[splittedLets[letter]]
                print(sum)
            elif splittedLets[letter] == "C" and (splittedLets[letter+1] == "D" or splittedLets[letter+1] == "M"):
                sum -= letToNum[splittedLets[letter]]
                print(sum)
            else:
                sum += letToNum[splittedLets[letter]]
                print(sum)

        # add the last element.
        # return the sum
            # necessary b/c for loop stops at the last character, by 'range(len(splittedLets)-1)' b/c if statements check for the i+1 character.
        sum += letToNum[splittedLets[-1]]
        print(sum)
        return sum


# CHATGPT SOLUTION

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        letToNum = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # similar to my situation, but consolidates the 3 if logic to just current_value and next_value variables.
        splittedLets = list(s)
        for i in range(len(splittedLets)-1):
            current_value = letToNum[splittedLets[i]]
            next_value = letToNum[splittedLets[i+1]]

            # If the current value is less than the next value, this means we have a subtraction scenario.
                # eg; MCM
                    # M = 1000, sum = 0 + 1000
                    # C = 100, but next character is greater than C, so subtract C from sum; 1000-100 = 900
                    # M = final character, stopped short, so just add by default, 900+1000 = 1900  
            if current_value < next_value:
                sum -= current_value
            else:
                sum += current_value
        
        # Add the last number as it's always added
        sum += letToNum[splittedLets[-1]]

        return sum

# Example usage:
sol = Solution()
result = sol.romanToInt("MCMXCIV")
print(result)  # Output: 1994
