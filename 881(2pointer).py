class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        boats =0
        l, r=0, len(p)-1
        while l<=r:
            wtAvailable = limit - p[r]
            r -= 1
            boats += 1
            if l <= r and p[l] <= wtAvailable:
                l += 1
    
        return boats
        