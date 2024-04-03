class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COLUMN = len(board), len(board[0])

        if len(word) > ROW*COLUMN:
            return False
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        pathCovered = set()
        def dfs(row, col, wordCheck):
            if wordCheck == len(word) : return True
            if (row<0 or row>=ROW or col<0 or col>=COLUMN or word[wordCheck]!=board[row][col] or (row,col) in pathCovered): return False
            pathCovered.add((row,col))
            result = (dfs(row+1,col,wordCheck+1) or
                      dfs(row-1,col,wordCheck+1) or
                      dfs(row,col+1,wordCheck+1) or
                      dfs(row,col-1,wordCheck+1))
            pathCovered.remove((row,col))
            return result
        for i in range(ROW):
            for j in range(COLUMN):
                if dfs(i,j,0) : return True
        return False