class Solution:
    def solution_863_2_1(self, s: str) -> int:
        
        if s == s[::-1]:
            return 0
        
        return len(s) - self.solution_863_2_2(s)
    
    
    def solution_863_2_2(self,s):
        
        revs = s[::-1]
        
        return self.solution_863_2_3(s,revs)
    
    
    def solution_863_2_3(self,a,b):
        
        n = len(a)
        m = len(b)
        
        if n==0 or m==0:
            return 0
        
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                    
        return dp[n][m]