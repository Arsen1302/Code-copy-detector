class Solution:
    def solution_803_4_1(self, grid: List[List[int]]) -> int:
        res = 0
        check = [ [False]*len(grid[0]) for _ in range(len(grid)) ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res = max(res, self.solution_803_4_2(grid,i,j,check))
        return res
    
    def solution_803_4_2(self, grid, i, j,check):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or check[i][j] or grid[i][j] == 0:
            return 0
            
        check[i][j] = True
        down = self.solution_803_4_2(grid, i+1, j, check)
        up = self.solution_803_4_2(grid, i-1, j, check)
        right = self.solution_803_4_2(grid, i, j+1, check)
        left = self.solution_803_4_2(grid, i, j-1, check)
        
        check[i][j] = False
        
        return max(down, max(up, max(left, right)))+grid[i][j]