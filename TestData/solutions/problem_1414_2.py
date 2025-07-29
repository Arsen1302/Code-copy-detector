class Solution:
    def solution_1414_2(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        ans = 0
        graph = collections.defaultdict(dict)
        for u,v,t in edges:
            graph[u][v] = t
            graph[v][u] = t
        
        # node, cost, visited, score
        q = collections.deque([(0, maxTime, set([0]), values[0])])
        while q:
            curr, cost, visited, score = q.popleft()
            if curr == 0:
                ans = max(ans, score)
            for nxt, time in graph[curr].items():
                if time > cost:
                    continue
                q.append((nxt, cost-time, visited|set([nxt]), score + values[nxt]*(nxt not in visited)))

        return ans