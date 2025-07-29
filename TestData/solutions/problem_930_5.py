class Solution:
    def solution_930_5(self, rating: List[int]) -> int:
        N = len(rating)
        dp = [[0] * N for _ in range(3)]

        for i in range(N):
            dp[0][i] = 1
        
        for i in range(1, 3):
            for j in range(i, N):
                for k in range(i - 1, j):
                    if rating[j] > rating[k]:
                        dp[i][j] += dp[i - 1][k] 
        
        r2 = rating[::-1]
        dp2 = [[0] * N for _ in range(3)]
        for i in range(N):
            dp2[0][i] = 1

        for i in range(1, 3):
            for j in range(i, N):
                for k in range(i - 1, j):
                    if r2[j] > r2[k]:
                        dp2[i][j] += dp2[i - 1][k]
        

        return sum(dp[-1]) + sum(dp2[-1])