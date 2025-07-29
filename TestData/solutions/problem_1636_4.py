class Solution:
    def solution_1636_4(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        ans = 0 
        seen = set(restricted)
        stack = [0]
        while stack: 
            u = stack.pop()
            ans += 1
            seen.add(u)
            for v in graph[u]: 
                if v not in seen: stack.append(v)
        return ans