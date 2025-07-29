class Solution:
    def solution_1372_3(self, n: int, rides: List[List[int]]) -> int:
        mp = {}
        for start, end, tip in rides: 
            mp.setdefault(start, []).append((end, tip))
        
        dp = [0]*(n+1)
        for x in range(n-1, 0, -1): 
            dp[x] = dp[x+1]
            for xx, tip in mp.get(x, []): 
                dp[x] = max(dp[x], xx - x + tip + dp[xx])
        return dp[1]