class Solution:
    def solution_303_3(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*amount
        for coin in coins: 
            for x in range(amount-coin+1): 
                dp[x+coin] += dp[x]
        return dp[-1]