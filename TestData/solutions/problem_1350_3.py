class Solution:
    def solution_1350_3(self, n: int, roads: List[List[int]]) -> int:
        
        neighbours = defaultdict(set)
        graph = [[0]*n for _ in range(n)]
        
        for u,v,d in roads:
            neighbours[u].add(v)
            neighbours[v].add(u)
            graph[u][v] = d
            graph[v][u] = d
        
        paths = defaultdict(int)
        paths[0] = 1
        distances = {i:inf for i in range(n)}
        q = [(0,0)]
        visited = set()
        while q:
            d,src = heapq.heappop(q)
            for nei in neighbours[src]:
                if nei not in visited:
                    if d+graph[src][nei] < distances[nei]:
                        distances[nei] = d+graph[src][nei]
                        heapq.heappush(q,(distances[nei],nei))
                        paths[nei] = paths[src]
                    elif d+graph[src][nei] == distances[nei]:
                        paths[nei] = paths[src] + paths[nei]
            visited.add(src)


        return paths[n-1]%(10**9+7)