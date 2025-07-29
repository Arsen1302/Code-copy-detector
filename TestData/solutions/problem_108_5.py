class Solution:
    def solution_108_5(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        dp = [[0]*n for _ in range(2)]  # 2-rowed dp array
        for i in range(m):
            for j in range(n):
                # i%2 (or i&amp;1) alternates between dp[0] and dp[1]
                dp[i%2][j] = 0 if matrix[i][j] == '0' else \
                    (min(dp[i%2][j-1] if j > 0 else 0,
                        dp[1-i%2][j-1] if j > 0 else 0,
                        dp[1-i%2][j]) + 1)
                result = dp[i%2][j] if dp[i%2][j] > result else result
        return result*result