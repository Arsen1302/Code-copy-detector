class Solution:
    def solution_411_5_1(self, grid: List[List[int]]) -> int:
        rowLength = len(grid[0])
        columnLength = len(grid)
        visited = {}
        
        def solution_411_5_2(i,j):
            if(i<0 or i>=columnLength or j<0 or j>=rowLength or grid[i][j] == 0 or (i,j) in visited):
                return 0
            visited[(i,j)] = True
            left = solution_411_5_2(i,j-1)
            right = solution_411_5_2(i,j+1)
            top = solution_411_5_2(i-1,j)
            bottom = solution_411_5_2(i+1,j)
            return 1 + left + right + top + bottom
        
        result = 0
        for i in range(columnLength):
            for j in range(rowLength):
                result = max(result,solution_411_5_2(i,j))
        
        return result