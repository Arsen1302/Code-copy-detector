class Solution:
    def solution_1102_5_1(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        parent = list(range(m*n))
        rank = [1 for _ in range(m*n)]
        def solution_1102_5_2(node):
            if parent[node]!=node:
                parent[node] = solution_1102_5_2(parent[node])
            return parent[node]
        def solution_1102_5_3(node1, node2):
            p1,p2 = solution_1102_5_2(node1),solution_1102_5_2(node2)
            if p1==p2:
                return
            if rank[p1]>rank[p2]:
                p1,p2 = p2,p1
            parent[p1] = p2
            rank[p2] += rank[p1]
        edges = []
        for i in range(m):
            for j in range(n):
                if i>0:
                    edges.append((abs(heights[i][j]-heights[i-1][j]),(i-1)*n+j,i*n+j))
                if j>0:
                    edges.append((abs(heights[i][j]-heights[i][j-1]),i*n+j-1,i*n+j))
        edges.sort()
        for t in edges:
            solution_1102_5_3(t[1],t[2])
            if solution_1102_5_2(0)==solution_1102_5_2(m*n-1):
                return t[0]
        return 0