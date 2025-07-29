class Solution(object):
    def solution_1603_5_1(self, n):
        ans = self.solution_1603_5_2(n, {})
		# n*2 plots
        return (ans*ans) % (10**9+7)
        
    def solution_1603_5_2(self, n, dp):
        state = n
        if n <= 1:
            return n+1
        if state in dp:
            return dp[state]
        else:
			#solution_1603_5_2 pattern
            ans =  self.solution_1603_5_2(n-1, dp) + self.solution_1603_5_2(n-2, dp) 
            
        dp[state] = ans
        return ans