class Solution:
def solution_830_1(self, grid: List[List[int]]) -> int:
    
    m,n = len(grid),len(grid[0])
    rows = [0]*m
    cols = [0]*n
    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                rows[i]+=1
                cols[j]+=1
                total+=1
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and rows[i]==1 and cols[j]==1:
                cnt+=1
    
    return total-cnt