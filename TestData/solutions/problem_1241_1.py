class Solution:
    def solution_1241_1(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[sys.maxsize] * n for _ in range(3)]
        dp[0][0]= 1
        dp[1][0]= 0
        dp[2][0]= 1
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] if obstacles[i] != 1 else sys.maxsize
            dp[1][i] = dp[1][i-1] if obstacles[i] != 2 else sys.maxsize
            dp[2][i] = dp[2][i-1] if obstacles[i] != 3 else sys.maxsize
            if obstacles[i] != 1:
                for j in [1, 2]:
                    dp[0][i] = min(dp[0][i], dp[j][i] + 1 if obstacles[i] != j+1 else sys.maxsize)
            if obstacles[i] != 2:
                for j in [0, 2]:
                    dp[1][i] = min(dp[1][i], dp[j][i] + 1 if obstacles[i] != j+1 else sys.maxsize)
            if obstacles[i] != 3:
                for j in [0, 1]:
                    dp[2][i] = min(dp[2][i], dp[j][i] + 1 if obstacles[i] != j+1 else sys.maxsize)
        return min(dp[0][-1], dp[1][-1], dp[2][-1])