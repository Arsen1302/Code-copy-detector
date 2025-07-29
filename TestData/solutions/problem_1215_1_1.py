class Solution:
    def solution_1215_1_1(self, n: int, edges: List[List[int]]) -> int:
        graph = {} # graph as adjacency list 
        for u, v, w in edges: 
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))
        
        queue = [n]
        dist = {n: 0}
        while queue: 
            newq = []
            for u in queue: 
                for v, w in graph[u]:
                    if v not in dist or dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w
                        newq.append(v)
            queue = newq
        
        @cache
        def solution_1215_1_2(u): 
            """Return number of restricted paths from u to n."""
            if u == n: return 1 # boundary condition 
            ans = 0
            for v, _ in graph[u]: 
                if dist[u] > dist[v]: ans += solution_1215_1_2(v)
            return ans 
        
        return solution_1215_1_2(1) % 1_000_000_007