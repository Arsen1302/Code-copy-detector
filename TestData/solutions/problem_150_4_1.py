class Solution:
    def solution_150_4_1(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        def solution_150_4_2(x): 
            """Return most distant node and trace."""
            queue = deque([x])
            trace = [-1] * n
            trace[x] = -2 
            while queue: 
                u = queue.popleft()
                for v in graph[u]: 
                    if trace[v] == -1: 
                        queue.append(v)
                        trace[v] = u
            return u, trace 
        
        x, _ = solution_150_4_2(0)
        x, trace = solution_150_4_2(x)
        vals = []
        while x >= 0: 
            vals.append(x)
            x = trace[x]
        k = len(vals)
        return vals[(k-1)//2 : k//2+1]