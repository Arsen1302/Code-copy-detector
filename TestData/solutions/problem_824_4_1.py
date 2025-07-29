class Solution:
    def solution_824_4_1(self, grid: List[List[int]]) -> int:
        # check if the input is valid
        numOfClosedIslands = 0
        if not grid or len(grid) == 0:
            return numOfClosedIslands
        
        nr = len(grid)
        nc = len(grid[0])
        
        for row in range(1, len(grid)-1):
            for column in range(1, len(grid[0])-1):
                if grid[row][column] == 0 and self.solution_824_4_2(grid, row, column, nr, nc):
                    numOfClosedIslands += 1
                    
        return numOfClosedIslands
    
    def solution_824_4_2(self, grid, row, column, nr, nc):
        
        
        if grid[row][column] == 1:
            return True
        
        if row <= 0 or row >= nr-1 or column <= 0 or column >= nc-1:
            return False
        
        grid[row][column] = 1
        up =self.solution_824_4_2(grid, row+1, column, nr, nc)
        down = self.solution_824_4_2(grid, row-1, column, nr, nc)
        left = self.solution_824_4_2(grid, row, column-1, nr, nc)
        right = self.solution_824_4_2(grid, row, column+1, nr, nc)
        
        return up and left and right and down