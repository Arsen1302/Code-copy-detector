class Solution:
    def solution_444_3(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [[sys.maxsize] * n for _ in range(n)]        
        graph = collections.defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))
            dp[s-1][e-1] = w
            
        for i in range(n):
            dp[i][i] = 0
            
        for kk in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][kk] != sys.maxsize and dp[kk][j] != sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[i][kk] + dp[kk][j])
        ans = 0                    
        for j in range(n):
            ans = max(ans, dp[k-1][j])
        return ans if ans != sys.maxsize else -1