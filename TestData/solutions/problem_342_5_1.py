class Solution:
def solution_342_5_1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    
    MOD = (10**9)+7
    dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
    
    def solution_342_5_2(i,j,maxMove):
        if maxMove<0:
            return 0
        
        if i<0 or i>=m or j<0 or j>=n:
            return 1
        
        if dp[i][j][maxMove] != -1:
            return dp[i][j][maxMove]
        
        a=solution_342_5_2(i-1, j, maxMove-1)
        b=solution_342_5_2(i+1, j, maxMove-1)
        c=solution_342_5_2(i, j-1, maxMove-1)
        d=solution_342_5_2(i, j+1, maxMove-1)
        
        dp[i][j][maxMove] = a+b+c+d
        return dp[i][j][maxMove]
    
    return solution_342_5_2(startRow,startColumn,maxMove)%MOD