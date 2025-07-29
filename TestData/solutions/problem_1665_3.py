class Solution:
    def solution_1665_3(self, I: List[List[int]]) -> int:
        max_val = max([v for _, v in I])
        dp = [0]*(max_val + 2)
        
        #Define intervals
        for u, v in I:
            dp[u] += 1
            dp[v + 1] -= 1
            
        #Compute prefix sum to get frequency
        for idx in range(1, len(dp)):
            dp[idx] += dp[idx - 1]
            
        #Return maximum overlap
        return max(dp)