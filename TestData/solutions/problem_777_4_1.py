class Solution:
def solution_777_4_1(self, grid: List[List[int]]) -> int:
    
    n = len(grid)
    q = []
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    
    def solution_777_4_2(i,j):
        if 0<=i<n and 0<=j<n and grid[i][j]==0:
            return True
        return False
    
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                q.append((i,j))
                dp[i][j]=0
    
    res = -1
    while q:
        x,y = q.pop(0)
        for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            if solution_777_4_2(x+dx,y+dy) and dp[x+dx][y+dy]==-1:
                q.append((x+dx,y+dy))
                dp[x+dx][y+dy] = dp[x][y]+1
                res = max(res,dp[x+dx][y+dy])
    
    return res