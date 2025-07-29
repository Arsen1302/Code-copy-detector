class Solution:
    def solution_1563_5(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1,n+1):
            c = s[i-1]
            count = 3
            if c in '7,9':count += 1
            
            for j in range(i-1,max(-1,i-count-1),-1):
                if s[j] != c:break
                dp[i] += dp[j]
            
            dp[i] %= (10**9+7)
            
        return dp[n]