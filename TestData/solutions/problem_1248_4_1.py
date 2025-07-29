class Solution:
    def solution_1248_4_1(self, tasks: List[List[int]]) -> List[int]:
        
        def solution_1248_4_2():
            import heapq
            nonlocal tasks
            tasks = [(*task, i) for i, task in enumerate(tasks)]
            tasks.sort()
            pq = []
            clk = tasks[0][0]
            i = 0
            while i < len(tasks) or pq:
                while i < len(tasks) and tasks[i][0] <= clk:
                    # as described, cpu would prefer tasks with shortest processing time.
                    # if multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
                    # since heappush does not support "key" function, 
                    # we push task into our heap as a tuple that consists of these two attributes
                    # in order to apply the sorting mechanism provided by python itself
                    heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                    i += 1
                if pq:
                    pt, pid = heapq.heappop(pq)
                    yield pid
                    clk += pt
                elif tasks[i][0] > clk:
                    clk = tasks[i][0]
        
        return list(solution_1248_4_2())