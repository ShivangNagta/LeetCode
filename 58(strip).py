class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        ansList = s.split(" ")
        return len(ansList[-1])