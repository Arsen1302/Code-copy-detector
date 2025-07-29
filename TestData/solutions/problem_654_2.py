class Solution:
    def solution_654_2(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0]*p[0] + p[1]*p[1])[:K]