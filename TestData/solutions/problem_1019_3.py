class Solution:
    def solution_1019_3(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for idx, (a, b) in enumerate(edges):
            c = -math.log(succProb[idx])
            graph[a].append((b, c))
            graph[b].append((a, c))
        visited = set()
        q = [(0, start)]
        while len(q) > 0:
            cost, node = heapq.heappop(q)
            if node == end:
                return 2.71828 ** (-cost)
            if node not in visited:
                visited.add(node)
                for nex, edge_cost in graph[node]:
                    heapq.heappush(q, (cost + edge_cost, nex))

        return 0