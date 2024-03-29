class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        start , end, ans = 0, 0, 0
        
        for i in range(len(nums)):
            countMax = 0
            for j in range(i, len(nums)):
                if nums[j] == maxElement:
                    countMax += 1
                if countMax >= k:
                    ans += 1
        
        return ans
