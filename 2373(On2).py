class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = []
        for i in range(n-2):
            temp = []
            for j in range(m-2):
                v1 = max(grid[i][j] , grid[i][j+1] , grid[i][j+2])
                v2 = max(grid[i+1][j] , grid[i+1][j+1] , grid[i+1][j+2])
                v3 = max(grid[i+2][j] , grid[i+2][j+1] , grid[i+2][j+2])

                temp.append(max(v1,v2,v3))
            ans.append(temp)

        return ans