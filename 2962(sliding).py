class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        start, end, countMax, ans = 0, 0, 0, 0
        while end < len(nums):
            if nums[end] == maxElement:
                countMax += 1
            while countMax >= k:
                ans += len(nums) - end
                if nums[start] == maxElement:
                    countMax -= 1
                start += 1
            end += 1
        return ans
