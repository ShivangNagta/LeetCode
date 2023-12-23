class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkDic = {}
        currentHighest = 0
        allHigh=[0] 
        for index,i in enumerate(s):
            if i in checkDic.keys():
                allHigh.append(currentHighest)
                currentHighest = index - checkDic[i]
                dicToListValues=[]
                for t in checkDic:
                    if checkDic[t]<checkDic[i]:
                        dicToListValues.append(t)
                for t in dicToListValues:
                    del checkDic[t]
                checkDic[i] = index
            else:
                currentHighest += 1
                checkDic[i]=index
        allHigh.append(currentHighest)        
        return max(allHigh)
     
obj=Solution()
print(obj.lengthOfLongestSubstring("abaab"))