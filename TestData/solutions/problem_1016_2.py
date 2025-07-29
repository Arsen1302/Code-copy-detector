class Solution:
    def solution_1016_2(self, n: int) -> bool:
        dp = [False] * (n+1)
        for x in range(1, n+1): 
            for k in range(1, int(sqrt(x))+1):
                if not dp[x-k*k]: 
                    dp[x] = True
                    break 
        return dp[-1]