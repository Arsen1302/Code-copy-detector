class Solution:
    def solution_515_5_1(self, grid: List[List[int]]) -> int:
        # inside dfs, update the area of the current island and
		# update the boundary cell to include this island as adjacent
        def solution_515_5_2(i, j):
            visited.add((i,j))
            areas[id] += 1
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if not grid[x][y]:
                        boundaries[(x,y)].add(id)
                    elif (x, y) not in visited:
                        solution_515_5_2(x, y)
        
        m, n = len(grid), len(grid[0])
        visited = set()
        boundaries = defaultdict(set)
        id, areas = 0, [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    solution_515_5_2(i, j)
                    id += 1
        
        if max(areas) == m * n:
            return m * n
        res = 0
        for p in boundaries:
            res = max(res, sum(areas[_] for _ in boundaries[p]))
        return res + 1