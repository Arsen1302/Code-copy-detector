class Solution:
    def solution_1091_5(self, n: int, roads: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(n)] 
        
        for s, d in roads:
            grid[s][d] = 1
            grid[d][s] = 1
        
        result = []
        visited = set()
        
        for s in range(n):
            for d in range(n):
                if s != d and (d, s) not in visited:
                    visited.add((s, d))
                    result.append(sum(grid[s]) + sum(grid[d]) - grid[s][d])
        return max(result)