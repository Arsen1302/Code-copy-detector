class Solution:
    def solution_458_5(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        for i, j in mines: dp[i][j] = 0
        
        for i in range(n):
            ll = dd = rr = uu = 0 
            for j in range(n): 
                dp[i][j] = min(dp[i][j], ll := ll+1 if dp[i][j] else 0)
                dp[j][i] = min(dp[j][i], dd := dd+1 if dp[j][i] else 0)
                dp[i][~j] = min(dp[i][~j], rr := rr+1 if dp[i][~j] else 0)
                dp[~j][i] = min(dp[~j][i], uu := uu+1 if dp[~j][i] else 0)
                    
        return max(map(max, dp))