class Solution:
    def solution_1282_2(self, servers: List[int], tasks: List[int]) -> List[int]:
        busy = []
        free = [(wt, i) for i, wt in enumerate(servers)]
        heapify(free)
        
        ans = []
        for t, task in enumerate(tasks): 
            while busy and busy[0][0] == t: 
                _, wt, i = heappop(busy)
                heappush(free, (wt, i))
            if free: wt, i = heappop(free)
            else: t, wt, i = heappop(busy)
            ans.append(i)
            heappush(busy, (t+task, wt, i))
        return ans