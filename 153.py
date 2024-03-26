class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end, ans = 0, len(nums) - 1 , nums[0]
        while (start <= end):
            mid = (start + end)>>1
            if nums[mid] >= nums[0]: start = mid+1
            else:
                ans = nums[mid]
                end = mid - 1
        return ans