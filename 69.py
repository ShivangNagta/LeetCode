class Solution:
    def mySqrt(self, x: int) -> int:
        start, end, ans = 1, x, 0
        while start <= end :
            mid = (start + end)>>1
            if mid*mid == x : return mid
            elif mid*mid < x:
                ans = mid
                start = mid +1
            elif mid*mid > x:
                end = mid -1
        return ans
