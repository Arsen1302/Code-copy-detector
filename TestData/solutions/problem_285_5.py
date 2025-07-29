class Solution:
    def solution_285_5(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0 # edge case (no attack)
        
        ans = 0
        for i in range(1, len(timeSeries)): 
            ans += min(timeSeries[i] - timeSeries[i-1], duration)
        return ans + duration