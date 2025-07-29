class Solution:
    def solution_1282_4(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans, avail, busy = [], [], []
        for i, w in enumerate(servers):
            avail.append([0, w, i])
        heapq.heapify(avail)
        
        for time, task in enumerate(tasks):
            
            while busy and busy[0][0] <= time:
                serv = heapq.heappop(busy)
                serv[0] = 0
                heapq.heappush(avail, serv)
            
            assign = heapq.heappop(avail) if avail else heapq.heappop(busy)
            ans.append(assign[2])
            assign[0] = max(time, assign[0]) + task
            heapq.heappush(busy, assign)
        
        return ans