class Solution:
    def solution_727_5(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [[0 for i in range(total//2+1)] for j in range(len(stones))]
        for i in range(len(stones)):
            for w in range(1,total//2+1):
                dp[i][w] = max(dp[i-1][w], ((stones[i] + dp[i-1][w-stones[i]]) if w>=stones[i] else 0))
        return total - dp[-1][-1]*2