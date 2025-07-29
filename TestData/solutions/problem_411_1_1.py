class Solution:
    def solution_411_1_1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # run solution_411_1_2 only when we find a land
                    maxArea = max(maxArea, self.solution_411_1_2(grid, i, j))
                    
        return maxArea
    
                    
    def solution_411_1_2(self, grid, i, j):
		# conditions for out of bound and when we encounter water
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return 0
        
        maxArea = 1
        grid[i][j] = '#'  # this will act as visited set
        maxArea += self.solution_411_1_2(grid, i+1, j)
        maxArea += self.solution_411_1_2(grid, i-1, j)
        maxArea += self.solution_411_1_2(grid, i, j+1)
        maxArea += self.solution_411_1_2(grid, i, j-1)
        
        return maxArea