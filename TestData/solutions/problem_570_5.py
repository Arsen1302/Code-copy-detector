class Solution:
    def solution_570_5(self, grid: List[List[int]]) -> int:
        t,s,f=0,0,0
        for i in range(len(grid)):
            maxRow,maxCol=0,0
            for j in range(len(grid[i])):
                if grid[i][j]>0:
                    t+=1
                maxRow=max(grid[i][j],maxRow)
                maxCol=max(grid[j][i],maxCol)
            s+=maxRow
            f+=maxCol
        return t+s+f