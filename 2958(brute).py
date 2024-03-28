class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ansList = []
        for i in range(len(nums)):
            repMap = {}
            for j in range(i,len(nums)):
                if k+1 in repMap.values():
                    ansList.append(sum(repMap.values())-1)
                    break
                if nums[j] in repMap.keys():
                    repMap[nums[j]]+=1
                else:
                    repMap[nums[j]] = 1
            if k+1 in repMap.values():
                ansList.append(sum(repMap.values())-1)
            else:
                ansList.append(sum(repMap.values()))
            
        return max(ansList)
