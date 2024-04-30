class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        maskStore = defaultdict(int)
        maskStore[0] = 1
        mask = 0

        for c in word:
            idx = ord(c) - ord('a')
            mask ^= (1 << idx)
            ans += maskStore[mask]

            for i in range(10):
                singleOddMask = (mask ^ (1 << i))
                ans += maskStore[singleOddMask]
                
            maskStore[mask] += 1

        return ans
