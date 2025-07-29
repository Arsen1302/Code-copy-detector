class Solution:
    def solution_468_4(self, grid: List[List[int]]) -> int:
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        n=len(grid)
        q=[[grid[0][0],0,0]]
        visit=set()
        while q:

            lvl,i,j=heapq.heappop(q)
            if i==n-1 and j==n-1:
                return lvl
            if (i,j) in visit:
                continue
            visit.add((i,j))
            for d in dir:
                x=i+d[0]
                y=j+d[1]
                if 0<=x<n and 0<=y<n and (x,y) not in visit: 
                    if grid[x][y]<=lvl:
                        heapq.heappush(q,[lvl,x,y])
                    else:
                        heapq.heappush(q,[lvl+abs(grid[x][y]-lvl),x,y])