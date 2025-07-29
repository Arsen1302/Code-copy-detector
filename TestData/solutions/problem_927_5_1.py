class Solution:
    def solution_927_5_1(self, grid: List[List[int]]) -> bool:
        self.m, self.n, self.res = len(grid), len(grid[0]), False
        self.vis = [[0] * (self.n) for _ in range(self.m)]
        
        def solution_927_5_2(x, y):
            return x >= 0 and x < self.m and y >= 0 and y < self.n
        
        # BFS - startPos: (startx, starty)
        def solution_927_5_3(startx, starty):
            que = [[startx, starty]]
            dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            self.vis[startx][starty] = 1
            while que:
                curx, cury = que.pop(0)
                if curx == self.m - 1 and cury == self.n - 1:
                    self.res = True; break
                for i in range(4):
                    nxtx, nxty = curx + dirr[i][0], cury + dirr[i][1]
                    # curPos(curx, cury) -> nxtPos(nxtx, nxty), both in the grid and are connected by the road
                    # if curDirection is ↑, then grid[curx][cury] should be 2 or 5 or 6, and grid[nxtx][nxty] should be 2 or 3 or 4
                    # if curDirection is ↓, then grid[curx][cury] should be 2 or 3 or 4, and grid[nxtx][nxty] should be 2 or 5 or 6
                    # if curDirection is ←, then grid[curx][cury] should be 1 or 3 or 5, and grid[nxtx][nxty] should be 1 or 4 or 6
                    # if curDirection is →, then grid[curx][cury] should be 1 or 4 or 6, and grid[nxtx][nxty] should be 1 or 3 or 5
                    if solution_927_5_2(nxtx, nxty) and self.vis[nxtx][nxty] == 0:
                        if (i == 0 and (grid[curx][cury] == 2 or grid[curx][cury] == 5 or grid[curx][cury] == 6) and (grid[nxtx][nxty] == 2 or grid[nxtx][nxty] == 3 or grid[nxtx][nxty] == 4)) or (i == 1 and (grid[curx][cury] == 2 or grid[curx][cury] == 3 or grid[curx][cury] == 4) and (grid[nxtx][nxty] == 2 or grid[nxtx][nxty] == 5 or grid[nxtx][nxty] == 6)) or (i == 2 and (grid[curx][cury] == 1 or grid[curx][cury] == 3 or grid[curx][cury] == 5) and (grid[nxtx][nxty] == 1 or grid[nxtx][nxty] == 4 or grid[nxtx][nxty] == 6)) or (i == 3 and (grid[curx][cury] == 1 or grid[curx][cury] == 4 or grid[curx][cury] == 6) and (grid[nxtx][nxty] == 1 or grid[nxtx][nxty] == 3 or grid[nxtx][nxty] == 5)):
                            self.vis[nxtx][nxty] = 1
                            que.append([nxtx, nxty])
                        
        solution_927_5_3(0, 0)
        return self.res