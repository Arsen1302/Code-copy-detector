class Solution:
    def solution_477_2(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = {}

        for u in range(n):
            graph[u] = []

        for u,v,w in flights:
            graph[u].append((v,w))

        heap = [(0,-K,src)]

        while heap:
            (cost,i,u) = heapq.heappop(heap)

            if u == dst:
                return cost

            for v,w in graph[u]:
                nc = cost + w

                if i <= 0:
                    heapq.heappush(heap, (nc,i+1,v))

        return -1