class Solution:
    def solution_1602_5(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        f=True
        for i in range(n):
                if grid[i][i] == 0 :
                    return False
                   
        
        for i in range(n):
                for j in range(n):
                    if i!=j and (i+j) != (n-1):
                        if grid[i][j] != 0:
                            return False
                            
                    if i+j == (n-1):
                        if grid[i][j] == 0:
                            return False
        return True