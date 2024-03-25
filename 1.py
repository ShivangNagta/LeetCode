class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkedDict={}
        for i,value in enumerate(nums):
            x=target-value
            if x in checkedDict.keys():
                return [i,checkedDict[x]]
            else:
                checkedDict[nums[i]]=i
  
        