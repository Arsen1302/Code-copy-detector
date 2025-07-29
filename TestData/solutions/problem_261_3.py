class Solution:
    def solution_261_3(self, grid: List[List[int]]) -> int:
        
        op = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                        dx = i + x
                        dy = j + y
                        # print(dx,dy)
                        if dx >= m or dy >= n or dx < 0 or dy < 0 or grid[dx][dy] == 0:
                            op += 1
                            
        return op