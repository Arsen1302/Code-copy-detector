class Solution:
    def solution_803_5_1(self, grid: List[List[int]]) -> int:
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        a_vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def solution_803_5_2(i,j):
            if(i <0 or j <0 or i == len(grid) or j == len(grid[0])):
                return False
            return True
        
        def solution_803_5_3(i, j, vis):
            sides = [[-1,0], [1,0], [0, 1], [0, -1]]
            retval = []
            for a,b in sides:
                x,y = a+ i, b+j
                if(solution_803_5_2(x, y) and not vis[x][y] and grid[x][y] !=0):
                    retval.append([x,y])
            return retval
        self.ans = 0
        def solution_803_5_4(grid, vis, i, j, cur):
            a_vis[i][j] = True
            cur += grid[i][j]
            self.ans = max(cur, self.ans)
            vis[i][j] = True
            for a, b in solution_803_5_3(i,j, vis):
                solution_803_5_4(grid, vis, a, b, cur)
            vis[i][j] = False
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(not a_vis[i][j]):
                    solution_803_5_4(grid, vis, i, j, 0)

        return self.ans