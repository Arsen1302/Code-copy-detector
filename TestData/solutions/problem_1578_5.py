class Solution:
    def solution_1578_5(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        for u, v in roads: 
            degree[u] += 1
            degree[v] += 1
        return sum(x*y for x, y in zip(range(1, n+1), sorted(degree)))