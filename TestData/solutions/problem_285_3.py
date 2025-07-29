class Solution:
    def solution_285_3(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0: return 0
        res = 0
        for i in range(len(timeSeries)-1):
            res += min(timeSeries[i] + duration, timeSeries[i+1]) - timeSeries[i]
        res += duration
        return res