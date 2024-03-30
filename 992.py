

class Solution:    
    def SlidingWindow(self, nums: List[int], k: int)-> int:
        left, right, ans = 0, 0, 0
        checkDic = {}
        while right < len(nums):
            checkDic[nums[right]] = checkDic.get(nums[right], 0) + 1
            while len(checkDic) > k:
                checkDic[nums[left]] -= 1
                if checkDic[nums[left]] == 0:
                    del checkDic[nums[left]]
                left += 1
            ans += right - left + 1
            right += 1
        return ans 

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.SlidingWindow(nums,k) - self.SlidingWindow(nums, k-1)

    