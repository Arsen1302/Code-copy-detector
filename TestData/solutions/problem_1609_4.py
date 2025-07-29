class Solution:
    def solution_1609_4(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        counts = [[1] * m for _ in range(n)]
        vertices = [(grid[i][j], i, j) for i in range(n) for j in range(m)]
        vertices.sort()
        for v, x, y in vertices:
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m and v > grid[nx][ny]:
                    counts[x][y] = (counts[x][y] + counts[nx][ny]) % (10**9 + 7)
        return sum(sum(counts[i]) for i in range(n)) % (10**9 + 7)