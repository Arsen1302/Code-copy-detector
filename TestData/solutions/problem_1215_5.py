class Solution:
    def solution_1215_5(self, n: int, edges: List[List[int]]) -> int:
        # Dijkstra's algorithm
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[n] = 0
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))
        pq = [(0, n)]
        while len(pq) > 0:
            curDistance, curVertex = heapq.heappop(pq)
			# skip the following steps if we've already visited the vertex
            if curDistance > distances[curVertex]:
                continue
            for edge in graph[curVertex]:
                neighbor = edge[0]
                weight = edge[1]
                distance = curDistance + weight
                # update neighbor's distance if the path via cur node has a shorter distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
		# Bottom-up DP
        # initialize dp array, which stores how many restricted paths between endnode and curnode
        dp = [0]*(n+1)
        dp[n] = 1
        dist = sorted(list(distances.keys()), key=lambda item:distances[item])
        for index in dist:
            neighbors = [edge[0] for edge in graph[index]]
            for neighbor in neighbors:
                if distances[neighbor] < distances[index]:
                    dp[index] += dp[neighbor]
                    dp[index] = int(dp[index]%(1e9+7))
            # when we've reached node 1 (start node), we could return the result
            if index == 1:
                return dp[1]
        return -1