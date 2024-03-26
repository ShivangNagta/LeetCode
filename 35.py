class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = len(nums)
        start, end = 0, len(nums) - 1
        while start<= end:
            mid = (start+end)>>1
            if nums[mid] == target : return mid
            elif nums[mid] < target : start = mid +1
            elif nums[mid] > target :
                end = mid - 1
                index = mid
        return index

