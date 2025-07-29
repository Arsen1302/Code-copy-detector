class Solution:
    def solution_882_5(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        for city1,city2,dist in edges:
            graph[city1].append((city2,dist))
            graph[city2].append((city1,dist))

        best_count = n+1
        city = -1
        for src_city in range(n):
            distance = [float("inf")]*n
            distance[src_city] = 0
            minHeap = []
            heappush(minHeap,(0,src_city))
            while minHeap:
                dist,node = heappop(minHeap)

                for nei_node,nei_dist in graph[node]:
                    new_dist = dist + nei_dist
                    if new_dist < distance[nei_node]:
                        distance[nei_node] = new_dist
                        heappush(minHeap,(new_dist,nei_node))
            count = 0
            for dist in distance:
                if dist <= distanceThreshold:
                    count += 1

            if count <= best_count:
                best_count = count
                city = src_city

        return city