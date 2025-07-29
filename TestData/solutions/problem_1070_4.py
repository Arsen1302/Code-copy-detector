class Solution:
    def solution_1070_4(self, points: List[List[int]]) -> int:
        N = len(points)
        
        adj = {i:[] for i in range(N)}
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dis = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])
        
        res = 0
        minHeap = [[0,0]]
        visit = set()
        while len(visit) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            for neighCost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neighCost, nei])
            visit.add(node)
        return res