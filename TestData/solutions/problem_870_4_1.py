class Solution:
    def solution_870_4_1(self, n: int, connections: List[List[int]]) -> int:

        def solution_870_4_2(node,  parent, vis, adj,check):

            vis[node] = True
            
            for i in adj[node]:
                #print(parent, node, i)
                if i == parent:
                    continue
                if vis[i] and i != parent:
                    #print(i,node)
                    if check[str(sorted([i,node]))] == 0:
                        solution_870_4_2.ans += 1
                        check[str(sorted([i,node]))] += 1
                elif not vis[i]:
                    solution_870_4_2(i, node, vis, adj, check)
                

        adj = [[] for i in range(n)]
        check = {}
        for i in connections:
            u = i[0]
            v = i[1]
            adj[u].append(v)
            adj[v].append(u)
            check[str(sorted([u,v]))] = 0
        #print(check)
        
        
        empty = -1
        parent = -1
        vis = [False for i in range(n)]
        solution_870_4_2.ans = 0
        
        for i in range(n):
            if not vis[i]:
                solution_870_4_2(i, parent, vis, adj, check)
                empty += 1
                
        if (solution_870_4_2.ans) >= empty:
            return empty
        return -1