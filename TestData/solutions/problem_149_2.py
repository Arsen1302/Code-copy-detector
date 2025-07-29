class Solution:
    def solution_149_2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(2)] for i in range(n+2)]
        
        dp[n][0] = dp[n][1] = 0
            
        ind = n-1
        while(ind>=0):
            
            dp[ind][1] = max(-prices[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
            
            dp[ind][0] = max(prices[ind] + dp[ind+2][1], 0 + dp[ind+1][0])
                    
            ind -= 1    
			
        return dp[0][1]