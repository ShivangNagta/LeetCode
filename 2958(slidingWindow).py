from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0 
        ans = 1
        repCheck = defaultdict(int)
        n = len(nums)
        while left < n and right < n:
            repCheck[nums[right]] +=1
            while repCheck[nums[right]] > k:
                repCheck[nums[left]] -=1
                left+=1
            ans = max(ans, right- left +1)
            right+=1
        return ans

