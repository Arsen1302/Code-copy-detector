class Solution:
    def solution_1715_5(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 1_000_000_007
        limit = high + 1 - min(zero, one)   # last dp array index to be processed
        dp_size = limit + max(zero, one)    # dp array size

        dp: List[int] = [0] * dp_size
        dp[0] = 1    

        for i in range(limit):
            if dp[i]:
                dp[i+zero] += dp[i] % MOD
                dp[i+one] += dp[i] % MOD

        return sum(dp[low:high+1]) % MOD