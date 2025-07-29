class Solution:
    def solution_1322_3(self, points: List[List[int]]) -> int:
        M = len(points)
        N = len(points[0])
        dp = [[0]*N for _ in range(M)]
        
        for i in range(N):
            dp[0][i] = points[0][i]
            
        for i in range(1, M):
            rollingMax = float('-inf')
            for j in range(N):
                rollingMax = max(rollingMax, dp[i-1][j] + j)
                dp[i][j] = points[i][j] + rollingMax - j
                
            rollingMax = float('-inf')
            for j in range(N-1, -1, -1):
                rollingMax = max(rollingMax, dp[i-1][j] - j)
                dp[i][j] = max(dp[i][j], points[i][j] + rollingMax + j)
            
        
        return max(dp[M-1])