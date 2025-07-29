class Solution:
    def solution_475_2_1(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        graph = [set(g) for g in graph]
        colors = [-1] * n
        def solution_475_2_2(i):
            q = collections.deque([[i, 0]])
            while q:
                idx, color = q.popleft()
                colors[idx] = color
                for nei in graph[idx]:
                    if colors[nei] >= 0:
                        if 1-color != colors[nei]: 
                            return False
                        continue
                    q.append((nei, 1-color))
            return True
        for i in range(n):
            if colors[i] < 0 and not solution_475_2_2(i):
                return False
        return True