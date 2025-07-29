class Solution:
    def solution_700_4_1(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        result = [0]
        
        def solution_700_4_2(i,j, isBoundary):
            if i < 0 or i >= m or j < 0 or j>= n or grid[i][j]!=1 or (i,j) in visited:
                return
            
            visited.add((i,j))
            if not isBoundary:
                result[0]+=1
            for x,y in [(0,-1), (0,1), (-1,0), (1,0)]:
                solution_700_4_2(i+x, j+y, isBoundary)
        
        
        for i in [0, m-1]:
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    solution_700_4_2(i,j, True)
                    
        for j in [0, n-1]:
            for i in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    solution_700_4_2(i,j, True)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    solution_700_4_2(i,j, False)
        
        return result[0]