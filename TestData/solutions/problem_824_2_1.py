class Solution:
    def solution_824_2_1(self, grid: List[List[int]]) -> int:
        result = 0
        
        def solution_824_2_2(grid, r, c):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
                return False
            if grid[r][c] != 0:
                return True
            
            grid[r][c] = 2
            return all([solution_824_2_2(grid, r - 1, c),
                        solution_824_2_2(grid, r + 1, c),
                        solution_824_2_2(grid, r, c - 1),
                        solution_824_2_2(grid, r, c + 1)])
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and solution_824_2_2(grid, r, c):
                    result += 1
        
        return result