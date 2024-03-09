class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        i = 0
        while i < len(strs)-1:
            if strs[i][i] == strs[i+1][i]:
                prefix += strs[i][i]
            else: 
                break
            i+=1

        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))