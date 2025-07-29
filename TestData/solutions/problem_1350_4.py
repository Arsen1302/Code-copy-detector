class Solution:
    def solution_1350_4(self, n: int, roads: List[List[int]]) -> int:
        time = [float("inf")]*n
        time[0] = 0
        ways = [0]*n
        ways[0] = 1

        minHeap = []
        
        heappush(minHeap,(0,0))

        graph = defaultdict(list)
        for road in roads:
            src,dst,t = road
            graph[src].append((t,dst))
            graph[dst].append((t,src))

        while minHeap:
            t,node = heappop(minHeap)

            for nei in graph[node]:
                nei_t,nei_node = nei
                new_time = t + nei_t

                if new_time == time[nei_node]:
                    ways[nei_node] += ways[node]

                if new_time < time[nei_node]:
                    time[nei_node] = new_time
                    heappush(minHeap,(new_time,nei_node))
                    ways[nei_node] = ways[node]

        return ways[n-1]%(10**9+7)