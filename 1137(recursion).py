class Solution:
    def Recursion(self,n):
        if n<=2:
            if n==0:
                return 0
            else:
                return 1
        else:
            return self.Recursion(n-1)+ self.Recursion(n-2)+ self.Recursion(n-3)

    def tribonacci(self, n: int) -> int:
        return self.Recursion(n)
        