class Solution:
def solution_674_4_1(self, grid: List[List[int]]) -> int:
    
    m,n,l = len(grid),len(grid[0]),0
    rot = []
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                rot.append([i,j,l])
            
    def solution_674_4_2(i,j,l):
        nonlocal rot
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
            return
        if grid[i][j]==1:
            rot.append([i,j,l+1])
            grid[i][j]=0
    
    while rot:
        a,b,l = rot.pop(0)
        grid[a][b] = 0
        solution_674_4_2(a+1,b,l)
        solution_674_4_2(a-1,b,l)
        solution_674_4_2(a,b+1,l)
        solution_674_4_2(a,b-1,l)    

    # Checking any 1 exist in grid
	for r in grid:
        if 1 in r:
            return -1
        
    return l