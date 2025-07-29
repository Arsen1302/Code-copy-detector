class Solution:
    def solution_579_5(self, grid: List[List[int]]) -> int:
        x, y, s = len(grid), len(grid[0]), 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] != 0:
                    s += 4 * grid[i][j] + 2
                    if j < y - 1:
                        s -= 2 * min(grid[i][j], grid[i][j+1])
                    if i < x - 1:
                        s -= 2 * min(grid[i][j], grid[i + 1][j])            
        return s