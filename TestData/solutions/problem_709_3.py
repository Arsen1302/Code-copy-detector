class Solution:
    def solution_709_3(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        return sum(a if i < len(costs)//2 else b for i, (a, b) in enumerate(costs))