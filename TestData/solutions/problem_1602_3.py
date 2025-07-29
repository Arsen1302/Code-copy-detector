class Solution:
    def solution_1602_3(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            if grid[i][i] == 0 or grid[i][len(grid)-1-i]==0:
                return False 
            for j in range(len(grid)):
                if j==i or j==len(grid)-1-i:
                    continue
                
                if grid[i][j] != 0:
                    return False
        return True