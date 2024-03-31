class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count , badi, mini, maxi = 0, -1, -1, -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK : badi = i
            if nums[i] == minK : mini = i
            if nums[i] == maxK : maxi = i
            count += max(0, min(mini,maxi) - badi)
        return count