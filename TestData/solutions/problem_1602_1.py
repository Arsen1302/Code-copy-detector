class Solution:
    def solution_1602_1(self, grid: List[List[int]]) -> bool:
        a=0
        j=len(grid)-1
        for i in range(0,len(grid)):
            if grid[i][i]==0 or grid[i][j]==0:
                return False
            else:
                if i!=j:
                    a=grid[i][i]+grid[i][j]
                elif i==j:
                    a=grid[i][i]
            if a!=sum(grid[i]):
                return False
            j-=1
        return True