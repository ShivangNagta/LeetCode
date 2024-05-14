class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
        for i in range(m):
            store = {0:0,1:0}
            for j in range(n):
                store[grid[j][i]]+=1
            storeVal = list(store.values())
            ans += max(storeVal)*(2**(m-i-1))

        return ans

        