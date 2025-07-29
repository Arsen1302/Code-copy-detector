class Solution:
    def solution_718_4(self, v: List[int]) -> int:
       
        
        dp = [[0 for i in range(len(v))] for j in range(len(v))]
        n = len(v)

        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                ans = float('inf')
                for k in range(i+1,j):
                    ans = min(ans, v[i]*v[j]*v[k] + dp[i][k] + dp[k][j])
                dp[i][j] = ans
        return dp[0][n-1]