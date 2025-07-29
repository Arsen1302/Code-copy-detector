class Solution:
    def solution_908_2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        i_curr, j_curr = 0, 0
        cost = 0
        frontier = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while 0 <= i_curr < m and 0 <= j_curr < n and not visited[i_curr][j_curr]:
            if i_curr == m - 1 and j_curr == n - 1:
                return cost
            visited[i_curr][j_curr] = True
            frontier.append((i_curr, j_curr))
            di, dj = dirs[grid[i_curr][j_curr] - 1]
            i_curr += di
            j_curr += dj
        while frontier:
            cost += 1
            next_layer = []
            for i, j in frontier:
                for di, dj in dirs:
                    i_next, j_next = i + di, j + dj
                    while 0 <= i_next < m and 0 <= j_next < n and not visited[i_next][j_next]:
                        if i_next == m - 1 and j_next == n - 1:
                            return cost
                        visited[i_next][j_next] = True
                        next_layer.append((i_next, j_next))
                        di, dj = dirs[grid[i_next][j_next] - 1]
                        i_next += di
                        j_next += dj
            frontier = next_layer