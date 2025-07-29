class Solution:
    def solution_1686_3(self, n: int, logs: List[List[int]]) -> int:
        startTime, maxTime, ans = 0, 0, 0
        for i, e in logs:
            t = e - startTime
            if t >= maxTime:
                ans = min(ans,i) if t == maxTime else i
                maxTime = t
            startTime = e
        return ans