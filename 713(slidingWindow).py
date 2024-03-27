class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<= 1 :
            return 0
        start, end, product, count = 0, 0, 1, 0
        while end < len(nums):
            product *= nums[end]
            while product >= k:
                product //= nums[start]
                start += 1
            count += end - start + 1
            end += 1
        return count