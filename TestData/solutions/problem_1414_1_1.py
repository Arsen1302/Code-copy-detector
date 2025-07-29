class Solution:
    def solution_1414_1_1(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        ans = 0
        graph = collections.defaultdict(dict)
        for u, v, t in edges:
            graph[u][v] = t
            graph[v][u] = t
        
        def solution_1414_1_2(curr, visited, score, cost):
            if curr == 0:
                nonlocal ans
                ans = max(ans, score)
            
            for nxt, time in graph[curr].items():
                if time <= cost:
                    solution_1414_1_2(nxt, visited|set([nxt]), score+values[nxt]*(nxt not in visited), cost-time)
        
        solution_1414_1_2(0, set([0]), values[0], maxTime)
        return ans