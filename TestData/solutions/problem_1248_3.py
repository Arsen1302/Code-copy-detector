class Solution:
    def solution_1248_3(self, tasks: List[List[int]]) -> List[int]:
        minHeap = []
        res = []
        for i in range(len(tasks)):
            tasks[i] += [i]
        tasks.sort(key=lambda x: x[0])
        t = tasks[0][0]
  
        while minHeap or tasks:
            while tasks and t >= tasks[0][0]:
                e_time, p_time, idx = tasks.pop(0)
                heapq.heappush(minHeap, [p_time, idx])
            if minHeap:
                p_time, idx = heapq.heappop(minHeap)
                t += p_time
                res.append(idx)
                continue
            t = tasks[0][0]      


        return res