class Solution:
    def solution_237_4(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        
        ans = 0
        endDate = intervals[0][1]
        for currentInterval in range(1, len(intervals)):
            if intervals[currentInterval][0] < endDate :
                ans += 1
                endDate = min(endDate, intervals[currentInterval][1])
            else:
                endDate = intervals[currentInterval][1]
        return ans