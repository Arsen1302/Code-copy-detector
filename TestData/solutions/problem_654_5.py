class Solution:
    def solution_654_5(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K, points, key=lambda x: x[0]**2 + x[1]**2)