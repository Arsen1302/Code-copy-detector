class Solution:
    def solution_251_3(self, points: List[List[int]]) -> int:
        points.sort()
        cur_end = -math.inf
        res = 0
        
        for start, end in points:
            if cur_end >= start:
                cur_end = min(cur_end, end)
            else:
                res += 1
                cur_end = end
        
        return res