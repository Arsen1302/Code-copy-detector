class Solution:
    def solution_842_5(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0], -x[1]))
        ans, right = 0, 0
        for u, v in intervals:
            if v > right:
                ans += 1
            right = max(right, v)
        return ans