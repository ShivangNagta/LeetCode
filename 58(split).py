class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ansList = s.split(" ")
        n = -1
        while ansList[n] == "":
            n = n -1 
        return len(ansList[n])