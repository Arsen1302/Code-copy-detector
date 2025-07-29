class Solution:
    def solution_1052_5_1(self, grid: List[List[str]]) -> bool:
        m,n = len(grid),len(grid[0])
        parent = list(range(m*n))
        rank = [1 for _ in range(m*n)]
        def solution_1052_5_2(node):
            if parent[node]!=node:
                parent[node] = solution_1052_5_2(parent[node])
            return parent[node]
        def solution_1052_5_3(node1,node2):
            p1,p2 = solution_1052_5_2(node1),solution_1052_5_2(node2)
            if p1==p2:
                return
            if rank[p1]>rank[p2]:
                p1,p2 = p2,p1
            rank[p2] += rank[p1]
            parent[p1] = p2
        for i in range(m):
            for j in range(n):
                for x,y in ((i,j+1),(i+1,j)):
                    if 0<=x<m and 0<=y<n and grid[i][j]==grid[x][y]:
                        n1,n2 = i*n+j,x*n+y
                        if solution_1052_5_2(n1)==solution_1052_5_2(n2):
                            return True
                        else:
                            solution_1052_5_3(n1,n2)
        return False