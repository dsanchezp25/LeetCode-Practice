class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
        number = i = 0
        while i < len(s):
            # if the actual number is higher than the next, we add the actual number only
            if i + 1 == len(s) or romanValues[s[i]] >= romanValues[s[i+1]]:
                number += romanValues[s[i]]
                i+=1
            else:
            # if the actual number is lower than the next, we add the subtraction : next-actual
                number += romanValues[s[i+1]] - romanValues[s[i]]
                i+=2
        return number
    
sol = Solution()
print(sol.romanToInt("MCMXCIV"))