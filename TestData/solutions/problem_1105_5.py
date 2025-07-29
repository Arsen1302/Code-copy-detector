class Solution:
    def solution_1105_5(self, points: List[List[int]]) -> int:
        xs = sorted({x[0] for x in points})
        if len(xs) == 1:
            return 0
        else:
            return max(xs[i+1]-xs[i] for i in range(0,len(xs)-1))