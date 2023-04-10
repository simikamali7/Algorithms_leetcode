# using a hashmap to solve

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     
    #  if their lengths are not same, then cannot be anagram
     if len(s) != len(t):
         return False
    
    # creating hashmaps
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)

    for i in range(len(t)):
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
        else:
            return True
    