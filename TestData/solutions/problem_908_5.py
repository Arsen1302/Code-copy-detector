class Solution:
    def solution_908_5(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        seen = set()
        queue = [(0, 0)]
        cost = 0
        
        while queue: #breadth-first search
            temp = set()
            for i, j in queue: 
                if i == m-1 and j == n-1: return cost
                if 0 <= i < m and 0 <= j < n and (i, j) not in seen: #skip invalid point
                    seen.add((i, j))
                    di, dj = direct[grid[i][j]-1]
                    queue.append((i+di, j+dj))
                    temp |= {(i+di, j+dj) for di, dj in direct}
            queue = list(temp - seen)
            cost += 1