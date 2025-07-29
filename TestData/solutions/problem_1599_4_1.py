class Solution:
    def solution_1599_4_1(self, n: int, edges: List[List[int]]) -> int:
        vis = [True]*n
        adj = [[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        components = []
        def solution_1599_4_2(v):
            if not vis[v]:
                return
            vis[v] = False
            components[-1] += 1
            for i in adj[v]:
                solution_1599_4_2(i)
        
        for vtx in range(n):
            if vis[vtx]:
                components.append(0)
                solution_1599_4_2(vtx)
        
        ans = 0
        curr = n
        for i in components:
            ans += (curr-i)*i
            curr -= i
        return ans