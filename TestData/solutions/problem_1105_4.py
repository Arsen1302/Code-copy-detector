class Solution:
    def solution_1105_4(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key = lambda x: x[0])
        prev = points[0][0]
        
        for x, y in points[1:]:
            res = max(res, x - prev)
            prev = x
        
        return res