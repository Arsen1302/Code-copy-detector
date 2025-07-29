class Solution:
    def solution_773_4(self, n: int, k: int, target: int) -> int:
        MOD = 1000 * 1000 * 1000 + 7 
        dp = defaultdict(int)
        dp[0] = 1 
        for c in range(n):
            sm = defaultdict(int)
            for i in range(target+1):
                sm[i] = sm[i-1] + dp[i]
            for i in range(target+1):
                dp[i] = (sm[i-1] - sm[i-k-1]) % MOD
        return dp[target]