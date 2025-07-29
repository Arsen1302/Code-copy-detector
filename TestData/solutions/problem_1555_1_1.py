class Solution:
    def solution_1555_1_1(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        vis = [[0]*n for _ in range(m)]
        # i - rows, j - colums
        # sum(row.count('hit') for row in grid)
        for i,j in walls:
            vis[i][j] = 2
        for i,j in guards:
            vis[i][j] = 2
        for i,j in guards:
            for l in range(j-1,-1,-1):
                if self.solution_1555_1_2(i,l,vis):
                    break    
                vis[i][l] = 1
            for r in range(j+1,n):
                if self.solution_1555_1_2(i,r,vis):
                    break
                vis[i][r] = 1
            for u in range(i-1,-1,-1):
                if self.solution_1555_1_2(u,j,vis):
                    break
                vis[u][j] = 1
            for d in range(i+1,m):
                if self.solution_1555_1_2(d,j, vis):
                    break
                vis[d][j] = 1
        return sum(row.count(0) for row in vis)
        
    def solution_1555_1_2(self, i, j, vis):
        if vis[i][j] ==2:
            return True