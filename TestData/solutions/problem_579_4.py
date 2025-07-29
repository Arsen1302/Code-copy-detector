class Solution:
    def solution_579_4(self, grid: List[List[int]]) -> int:
        area = 0
        rows1, cols1 = len(grid) - 1, len(grid[0]) - 1
        for r, row in enumerate(grid):
            for c, height in enumerate(row):
                area += 2 * (height > 0)
                if r == 0 and c == 0:
                    area += 2 * height
                elif r == 0 and c > 0:
                    area += height + abs(height - grid[0][c - 1])
                elif c == 0 and r > 0:
                    area += height + abs(height - grid[r - 1][0])
                else:
                    area += (abs(height - grid[r][c - 1]) +
                             abs(height - grid[r - 1][c]))
                if r == rows1 and c == cols1:
                    area += 2 * height
                elif r == rows1 or c == cols1:
                    area += height
        return area