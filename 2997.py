class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for bit in range(20):
            xorVal = 0
            for i in nums:
                xorVal ^= ((1<<bit) & i)
            kbitVal = (1<<bit) & k
            if kbitVal != xorVal:
                count+=1


        return count