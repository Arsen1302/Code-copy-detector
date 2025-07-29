class Solution:
    def solution_700_5_1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        
        def solution_700_5_2(r, c, value):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = value
            solution_700_5_2(r - 1, c, value)
            solution_700_5_2(r + 1, c, value)
            solution_700_5_2(r, c + 1, value)
            solution_700_5_2(r, c - 1, value)
            
        for r in range(rows):
            solution_700_5_2(r, 0, 0)
            solution_700_5_2(r, cols - 1, 0)

        for c in range(cols):
            solution_700_5_2(0, c, 0)
            solution_700_5_2(rows - 1, c, 0)
        count = 0
		
        return sum([1 for r in range(rows) for c in range(cols) if grid[r][c] == 1])