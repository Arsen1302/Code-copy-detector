class Solution:
    def solution_237_1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        ans, curr = 1, intervals[0]

        for i in range(n):
            if intervals[i][0] >= curr[1]:
                ans += 1
                curr = intervals[i]

        return n - ans