class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        maxAns = 0
        for i in range(len(s)):
            if s[i] == "(": 
                ans+=1
                if maxAns < ans: maxAns = ans
            if s[i] == ")": 
                ans-=1
        return maxAns