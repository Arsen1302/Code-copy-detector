class Solution:
    def solution_1215_2_1(self, n: int, edges: List[List[int]]) -> int:
        graph = {} # graph as adjacency list 
        for u, v, w in edges: 
            graph.setdefault(u-1, []).append((v-1, w))
            graph.setdefault(v-1, []).append((u-1, w))
        
        # dijkstra's algo
        pq = [(0, n-1)]
        dist = [inf]*(n-1) + [0]
        while pq: 
            d, u = heappop(pq)
            for v, w in graph[u]: 
                if dist[u] + w < dist[v]: 
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        
        @cache
        def solution_1215_2_2(u): 
            """Return number of restricted paths from u to n."""
            if u == n-1: return 1 # boundary condition 
            ans = 0
            for v, _ in graph[u]: 
                if dist[u] > dist[v]: ans += solution_1215_2_2(v)
            return ans 
        
        return solution_1215_2_2(0) % 1_000_000_007