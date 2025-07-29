class Solution:
    def solution_374_5(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        N = len(pairs)

        dp = [1] * (N + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(i):
                if pairs[j - 1][1] < pairs[i - 1][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp[-1]