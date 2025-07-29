class Solution:
    def solution_1390_1(self, grid: List[List[int]], x: int) -> int:
        vals = [x for row in grid for x in row]
        if len(set(val%x for val in vals)) > 1: return -1 # impossible
        median = sorted(vals)[len(vals)//2] # O(N) possible via "quick select"
        return sum(abs(val - median)//x for val in vals)