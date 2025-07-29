class Solution:
    def solution_713_2_1(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        rows,cols = len(grid),len(grid[0])
        queue = [(row,col)]
        oldColor = grid[row][col]
        
        vis =  [[False for i in range(cols)] for j in range(rows)]
        vis[row][col] = True
        toChange = [[False for i in range(cols)] for j in range(rows)]
        
        def solution_713_2_2(r,c):
            if (r == 0 or grid[r-1][c] != oldColor) or (r == rows-1 or grid[r+1][c] != oldColor) \
            or (c == 0 or grid[r][c-1] != oldColor) or (c == cols-1 or grid[r][c+1] != oldColor):
                return True
            return False
        
        while queue:
            r,c = queue.pop(0)
            
            if solution_713_2_2(r,c) == True: toChange[r][c] = True
            
            for x,y in ((r+1,c),(r-1,c),(r,c-1),(r,c+1)):
                
                if 0<=x<rows and 0<=y<cols and grid[x][y] == oldColor and not vis[x][y]:                  
                    vis[x][y] = True
                    queue.append((x,y))
        
        for i in range(rows):
            for j in range(cols):
                if toChange[i][j] == True:
                    grid[i][j] = color
        
        return grid