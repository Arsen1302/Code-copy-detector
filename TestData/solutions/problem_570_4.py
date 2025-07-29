class Solution:
    def solution_570_4(self, grid: List[List[int]]) -> int:
        n=len(grid)
        area=0
        for i in range(n):
            maxVal1=0
            maxVal2=0
            for j in range(n):
                if grid[i][j]>maxVal1:
                    maxVal1=grid[i][j]
                if grid[j][i]>maxVal2:
                    maxVal2=grid[j][i]
                if grid[i][j]>0:
                    area+=1
            area+=maxVal1+maxVal2 
        return area