class Solution:
    def solution_1402_2(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indeg = [0]*n 
        for u, v in relations: 
            graph[u-1].append(v-1)
            indeg[v-1] += 1
        
        start = [0]*n
        queue = deque((i, time[i]) for i, x in enumerate(indeg) if x == 0)
        
        while queue: 
            u, t = queue.popleft() # earlist to finish course u
            for v in graph[u]: 
                start[v] = max(start[v], t) # earlist to start course v
                indeg[v] -= 1
                if indeg[v] == 0: queue.append((v, start[v] + time[v]))
        return max(s+t for s, t in zip(start, time))