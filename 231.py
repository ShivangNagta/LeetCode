from math import log2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and log2(n)-int(log2(n)) == 0.0:
            return True
        else:
            return False
        