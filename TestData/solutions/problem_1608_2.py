class Solution:
    def solution_1608_2(self, n: int, delay: int, forget: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n+1):
            if dp[i] > 0:
                lower = i + delay # 3
                upper = i + forget
                upper_bound = min(upper, n+1)
                for j in range(lower, upper_bound):
                    dp[j] += dp[i]

                if upper <= n:
                    dp[i] = 0
        
        print(dp)
        return sum(dp) % (10**9 + 7)