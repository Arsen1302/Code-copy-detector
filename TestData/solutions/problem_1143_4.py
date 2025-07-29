class Solution:
    def solution_1143_4(self, stones: List[int]) -> int:
        prefix = [0]
        for x in stones: prefix.append(prefix[-1] + x)
            
        n = len(stones)
        dp = [[0]*n for _ in range(n)]
        for i in reversed(range(n)): 
            for j in range(i+1, n): 
                dp[i][j] = max(prefix[j+1] - prefix[i+1] - dp[i+1][j], prefix[j] - prefix[i] - dp[i][j-1])
        return dp[0][-1]