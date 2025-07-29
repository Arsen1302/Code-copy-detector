class Solution:
    def solution_238_5(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = []

        for interval in intervals:
            rightInterval = bisect.bisect_left(starts, interval[1], key=lambda x: x[0])
            res.append(starts[rightInterval][1] if rightInterval != n else -1)
        
        return res