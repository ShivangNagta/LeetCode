class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checkMap = {}
        for i in range(len(s)):
            if s[i] in checkMap.keys():
                if checkMap[s[i]] == t[i]:
                    pass
                else:
                    return False
            else:
                if t[i] in checkMap.values():
                    return False
                else:
                    checkMap[s[i]] = t[i]
        return True
