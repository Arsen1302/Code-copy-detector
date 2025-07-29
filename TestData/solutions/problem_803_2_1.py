class Solution:
    def solution_803_2_1(self):
        self.max_gold = 0
        
    def solution_803_2_2(self, grid, i, j, cur_gold):
        cur_val = grid[i][j]
        grid[i][j] = 0
        
        if i > 0 and grid[i - 1][j] != 0:
            self.solution_803_2_2(grid, i - 1, j, [cur_gold[0] + cur_val])
        if i < len(grid) - 1 and grid[i + 1][j] != 0:
            self.solution_803_2_2(grid, i + 1, j, [cur_gold[0] + cur_val])
        if j > 0 and grid[i][j - 1] != 0:
            self.solution_803_2_2(grid, i, j - 1, [cur_gold[0] + cur_val])
        if j < len(grid[0]) - 1 and grid[i][j + 1] != 0:
            self.solution_803_2_2(grid, i, j + 1, [cur_gold[0] + cur_val])
        
        self.max_gold = max(self.max_gold, cur_gold[0] + cur_val)
        grid[i][j] = cur_val
        
    def solution_803_2_3(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    self.solution_803_2_2(grid, i, j, [0])
        
        return self.max_gold