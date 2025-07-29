class Solution:
    def solution_227_5_1(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        
        def solution_227_5_2(i, j): 
            """Traverse the grids connected to (i, j)."""
            board[i][j] = "." # mark as visited 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == "X": solution_227_5_2(ii, jj)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X": 
                    ans += 1
                    solution_227_5_2(i, j)
        return ans