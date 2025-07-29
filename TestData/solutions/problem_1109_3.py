class Solution:
    def solution_1109_3(self, k: int) -> int:        
        dp = [1] * 5
                                
        for _ in range(1, k):
            for i in range(1, 5):                    
                dp[i] = dp[i] + dp[i-1]
        
        return sum(dp)