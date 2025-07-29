class Solution:
    def solution_1578_4(self, n: int, roads: List[List[int]]) -> int:
        in_deg = [0]*n
        for u, v in roads:
            in_deg[u] += 1
            in_deg[v] += 1
        
        return sum([deg*i for i, deg in enumerate(sorted(in_deg), start=1)])