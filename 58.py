class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counting = False
        ans = 0
        for i in range(len(s)):
            if s[len(s) - i - 1] != " ":
                counting = True
                ans += 1
            elif (counting): break
        return ans