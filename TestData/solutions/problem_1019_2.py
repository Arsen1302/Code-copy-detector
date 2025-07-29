class Solution:
    def solution_1019_2(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # construct the graph
        graph = collections.defaultdict(list)
        prob = collections.defaultdict(dict)
        for i,(p,[a,b]) in enumerate(zip(succProb,edges)):
            graph[a].append(b)
            graph[b].append(a)
            prob[a][b] = prob[b][a] = p
        # apply dijkstra
        dis = {start:1}
        for i in range(n):
            dis[i] = 0
        visited = set([])
        # note that Python only supports min-heap
        # so some tricks here to get a max-heap
        pq = [(-1,start)]
        while pq:
            _p, node = heapq.heappop(pq)
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    if dis[child] < -1 * _p * prob[node][child]:
                        heapq.heappush(pq,(_p * prob[node][child],child))
                        dis[child] = -1 * _p * prob[node][child]

        return dis[end]