class Solution:
    def solution_1282_3(self, servers: List[int], tasks: List[int]) -> List[int]:
        ns = len(servers)
        nt = len(tasks)
        
        free = [] # (weight, index, time), sort by weight
        for i in range(ns):
            heapq.heappush(free, (servers[i], i, 0))
            
        busy = [] # (time, weight, index), sort by time
        
        result = []
        
        for j in range(nt):
            # move finished server from busy to free
            while len(busy)> 0 and busy[0][0] <= j:
                time, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index, time))
                
            # assign new task
            if len(free) > 0:
                weight, index, time = heapq.heappop(free)
            else:
                time, weight, index = heapq.heappop(busy)
            result.append(index)
            
            # why time = max(time, j)?
            # case1:
            # there are free servers, add time to the first free server
            # e.g. j = 2, tasks[j] = 3, 
            #      free[0] = (3, 0, 0) -> busy[0] = (5, 3, 0)
            
            # case2:
            # no free server, the first server in busy is still working, add time to the first busy server
            # e.g. j = 2, tasks[j] = 3,
            #      busy[0] = (3, 3, 0), still working
            #   -> busy[0] = (6, 3, 0)
            time = max(time, j) 
            # move assigned server from free to busy
            heapq.heappush(busy, (time + tasks[j], weight, index))
            
        return result