class Solution:
    def solution_1313_5(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows=len(maze)
        cols=len(maze[0])
        sx,sy=entrance
        maze[sx][sy]='s'
        for x in range(rows):
            if maze[x][0]=='.':
                maze[x][0]='e'
            if maze[x][-1]=='.':
                maze[x][-1]='e'
        for y in range(cols):
            if maze[0][y]=='.':
                maze[0][y]='e'
            if maze[-1][y]=='.':
                maze[-1][y]='e'
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        
        done=[[False]*cols for _ in range(rows)]
        queue=collections.deque()
        queue.append((0,sx,sy))
        done[sx][sy]=True
        while len(queue)>0:
            d,x,y=queue.popleft()
            for dx,dy in dir:
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny < cols and not done[nx][ny]:
                    if maze[nx][ny]==".":
                        queue.append((d+1,nx,ny))
                    elif maze[nx][ny] =="e":
                        return d+1


        return -1
            
                               # [6] BFS failed, there is no escape