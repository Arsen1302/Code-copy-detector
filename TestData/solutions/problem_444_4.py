class Solution:
    def solution_444_4(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [sys.maxsize] * n
        dp[k-1] = 0
        
        for _ in range(n-1):
            for s, e, w in times:
                if dp[e-1] > dp[s-1] + w:
                    dp[e-1] = dp[s-1] + w
                    
        ans = 0                    
        for i in range(n):
            if i != k-1:
                ans = max(ans, dp[i])
        return ans if ans != sys.maxsize else -1