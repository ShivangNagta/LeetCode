
from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            d = defaultdict(int)
            for j in range(i, len(word)):
                d[word[j]] += 1
                dVal = d.values()
                countOdd = sum(1 for x in dVal if (1&x) !=0)
                if countOdd <= 1:
                    ans +=1
        return ans
