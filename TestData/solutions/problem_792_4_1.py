class Solution:
    def solution_792_4_1(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {} # graph as adjacency list 
        for u, v in connections: 
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        def solution_792_4_2(x, p, step): 
            """Traverse the graph and collect bridges using Tarjan's algo."""
            disc[x] = low[x] = step
            for xx in graph.get(x, []): 
                if disc[xx] == inf: 
                    step += 1
                    solution_792_4_2(xx, x, step)
                    low[x] = min(low[x], low[xx])
                    if low[xx] > disc[x]: ans.append([x, xx]) # bridge
                elif xx != p: low[x] = min(low[x], disc[xx])
        
        ans = []
        low = [inf]*n
        disc = [inf]*n
        
        solution_792_4_2(0, -1, 0)
        return ans