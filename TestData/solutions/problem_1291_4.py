class Solution:
    def solution_1291_4(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[(0, 0, 0, 0)] * (n+1) for _ in range(m+1)] # [prefix-row-sum, prefix-col-sum, prefix-major-diagonal, prefix-minor-diagonal]
        for i in range(1, m+1):                           # O(m*n) on prefix calculation
            for j in range(1, n+1):
                dp[i][j] = [
                    dp[i][j-1][0] + grid[i-1][j-1], 
                    dp[i-1][j][1] + grid[i-1][j-1],
                    dp[i-1][j-1][2] + grid[i-1][j-1],
                    (dp[i-1][j+1][3] if j < n else 0) + grid[i-1][j-1],
                ]
        for win in range(min(m, n), 0, -1):                 # for each edge size (window size)
            for i in range(win, m+1):                       # for each x-axis
                for j in range(win, n+1):                   # for each y-axis
                    val = dp[i][j][2] - dp[i-win][j-win][2] # major diagonal
                    if dp[i][j-win+1][3] - (dp[i-win][j+1][3] if j+1 <= n else 0) != val: continue            # minor diagonal
                    if any(dp[row][j][0] - dp[row][j-win][0] != val for row in range(i, i-win, -1)): continue # for each row
                    if any(dp[i][col][1] - dp[i-win][col][1] != val for col in range(j, j-win, -1)): continue # for each col
                    return win    
        return 1