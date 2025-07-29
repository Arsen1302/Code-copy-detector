class Solution:
    def solution_210_1_1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (u, v), w in zip(equations, values): 
            graph.setdefault(u, []).append((v, 1/w))
            graph.setdefault(v, []).append((u, w))

        def solution_210_1_2(n, g, val=1):
            """Depth-first traverse the graph."""
            if n in vals: return 
            vals[n] = val, g
            for nn, w in graph.get(n, []): solution_210_1_2(nn, g, w*val)
    
        vals = dict()
        for i, n in enumerate(graph): solution_210_1_2(n, i)
        
        ans = []
        for u, v in queries: 
            if u in vals and v in vals and vals[u][1] == vals[v][1]: ans.append(vals[u][0]/vals[v][0])
            else: ans.append(-1)
        return ans