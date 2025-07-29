class Solution:
    def solution_1019_4(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        #create adjList
        adjList = {i:[] for i in range(n)}
        for directions, prob in zip(edges, succProb):
            adjList[directions[0]].append([directions[1], -1*prob])
            adjList[directions[1]].append([directions[0], -1*prob])
        #create minHeap
        maxHeap = []
        maxHeap.append([-1, start])
        heapq.heapify(maxHeap)
        #dijkstra
        finalProb = [0] * n
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            for it in adjList[node]:
                edgeProb = -1 * it[1]
                edgeNode = it[0]
                if prob*edgeProb < finalProb[edgeNode]:
                    finalProb[edgeNode] = prob*edgeProb
                    heapq.heappush(maxHeap, [prob*edgeProb, edgeNode])
                    
        return -1*finalProb[end]