class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            idx = word.index(ch)
            prefix = word[:idx+1]
            if idx+1 < len(word):
                suffix = word[idx+1:]
            else:
                suffix = ''
            return prefix[::-1]+suffix
        return word