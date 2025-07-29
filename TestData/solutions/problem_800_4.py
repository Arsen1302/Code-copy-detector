class Solution:
    def solution_800_4(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = {(0, 0, 0, 1): 0}
        pq = [(0, 0, 0, 0, 1)]
        while pq: 
            x, i, j, ii, jj = heappop(pq)
            if i == n-1 and j == n-2 and ii == n-1 and jj == n-1: return x
            if ii+1 < n and grid[i+1][j] == grid[ii+1][jj] == 0 and x+1 < dist.get((i+1, j, ii+1, jj), inf): 
                heappush(pq, (x+1, i+1, j, ii+1, jj))
                dist[i+1, j, ii+1, jj] = x + 1
            if jj+1 < n and grid[i][j+1] == grid[ii][jj+1] == 0 and x+1 < dist.get((i, j+1, ii, jj+1), inf): 
                heappush(pq, (x+1, i, j+1, ii, jj+1))
                dist[i, j+1, ii, jj+1] = x + 1
            if i == ii and ii+1 < n and grid[i+1][j] == grid[i+1][jj] == 0 and x+1 < dist.get((i, j, i+1, j), inf): 
                heappush(pq, (x+1, i, j, i+1, j))
                dist[i, j, i+1, j] = x + 1
            if j == jj and jj+1 < n and grid[i][j+1] == grid[ii][j+1] == 0 and x+1 < dist.get((i, j, i, j+1), inf): 
                heappush(pq, (x+1, i, j, i, j+1))
                dist[i, j, i, j+1] = x + 1
        return -1