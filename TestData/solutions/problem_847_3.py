class Solution:
    def solution_847_3(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        ans = 1
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = k
        queue = [(0, 0, k)]
        while queue:
            tmp = []
            for i in queue:
                for x, y in [(i[0] - 1, i[1]), (i[0], i[1] - 1), (i[0] + 1, i[1]), (i[0], i[1] + 1)]:
                    if 0 <= x < m and 0 <= y < n and i[2] >= grid[x][y] and i[2] - grid[x][y] > visited[x][y]:
                        visited[x][y] = (i[2] - grid[x][y])
                        tmp.append((x, y, i[2] - grid[x][y]))
                        if x == m - 1 and y == n - 1:
                            return ans
            queue = tmp
            ans += 1
        return -1