class Solution:
    def solution_522_5(self, n: int, edges: List[List[int]]) -> List[int]:
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for s,e in edges:
            dp[s][e] = 1
            dp[e][s] = 1
            
        for i in range(n):
            dp[i][i] = 0
        
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])    
                        
    
        ans = []
        
        for i in range(n):
            s = 0 
            for j in range(n):
                s += dp[i][j] if dp[i][j] != float('inf') else 0
                
            ans.append(s)
            
        return ans