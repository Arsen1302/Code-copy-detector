class Solution:
    def solution_1313_2(self, grid: List[List[str]], entrance: List[int]) -> int:
        m=len(grid)
        n=len(grid[0])
        lst=[[entrance[0],entrance[1],0]]
        visited=[[-1]*n for i in range(m)]
        row=[-1,1,0,0]
        col=[0,0,-1,1]
        visited[entrance[0]][entrance[1]]=1
        while lst:
            x,y,d=lst.pop(0)
            for i in range(4):
                if x+row[i]>=0 and x+row[i]<m and y+col[i]>=0 and y+col[i]<n and visited[x+row[i]][y+col[i]]==-1 and grid[x+row[i]][y+col[i]]=='.':
                    if x+row[i]==0 or x+row[i]==m-1 or y+col[i]==0 or y+col[i]==n-1:
                        return d+1
                    lst.append([x+row[i],y+col[i],d+1])
                    visited[x+row[i]][y+col[i]]=1
        return -1