class Solution:
    def solution_579_3(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0 if grid[0][0] == 0 else 2 * (2 * grid[0][0] + 1)
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    count += 2 * (2 * grid[i][j] + 1)
        for i in range(n):
            for j in range(n):
                x = 0
                if i == 0:
                    if grid[i+1][j] != 0:
                        x += min(grid[i+1][j], grid[i][j])
                    if j == 0:
                        if grid[i][j+1] != 0:
                            x += min(grid[i][j], grid[i][j+1])
                    elif j == n-1:
                        if grid[i][j-1] != 0:
                            x += min(grid[i][j], grid[i][j-1])
                    else:
                        if grid[i][j+1] != 0:
                            x += min(grid[i][j], grid[i][j+1])
                        if grid[i][j-1] != 0:
                            x += min(grid[i][j], grid[i][j-1])
                elif i == n-1:
                    if grid[i-1][j] != 0:
                        x += min(grid[i-1][j], grid[i][j])
                    if j == 0:
                        if grid[i][j+1] != 0:
                            x += min(grid[i][j], grid[i][j+1])
                    elif j == n-1:
                        if grid[i][j-1] != 0:
                            x += min(grid[i][j], grid[i][j-1])
                    else:
                        if grid[i][j+1] != 0:
                            x += min(grid[i][j], grid[i][j+1])
                        if grid[i][j-1] != 0:
                            x += min(grid[i][j], grid[i][j-1])
                
                else:
                    if grid[i-1][j] != 0:
                        x += min(grid[i-1][j], grid[i][j])
                    if grid[i+1][j] != 0:
                        x += min(grid[i+1][j], grid[i][j])
                    if j == 0:
                        if grid[i][j+1] != 0:
                            x += min(grid[i][j], grid[i][j+1])
                    elif j == n-1:
                        if grid[i][j-1] != 0:
                            x += min(grid[i][j], grid[i][j-1])
                    else:
                        if grid[i][j+1] != 0:
                            x += min(grid[i][j], grid[i][j+1])
                        if grid[i][j-1] != 0:
                            x += min(grid[i][j], grid[i][j-1])
                count -= x
        return count