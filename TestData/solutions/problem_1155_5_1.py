class Solution:
    def solution_1155_5_1(self,x,y,m,n,grid,visited):
        if visited[x][y]!=None:
            return visited[x][y]
        if y+grid[x][y]<0 or y+grid[x][y]>=n or (grid[x][y]+grid[x][y+grid[x][y]]==0):
            visited[x][y]=-1
            return -1
        visited[x][y]=y+grid[x][y]
        if x+1<m:
            return self.solution_1155_5_1(x+1,y+grid[x][y],m,n,grid,visited)
        else:
            return visited[x][y]
                
    def solution_1155_5_2(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])
        visited=[[None]*n for _ in range(m)]
        result=[]
        for i in range(n):
            x=self.solution_1155_5_1(0,i,m,n,grid,visited)
            result.append(x)
        return result