class Solution:
    def solution_1630_1_1(self, edges: List[int]) -> int:
        in_d = set()
        out_d = set()
        for i, j in enumerate(edges):
            if j != -1:
                in_d.add(j)
                out_d.add(i)
        potential = in_d &amp; out_d
        visited = set()
        self.ans = -1
        def solution_1630_1_2(node, curr, v):
            visited.add(node)
            v[node] = curr
            nei = edges[node]
            if nei in v:
                self.ans = max(self.ans, curr - v[nei] + 1)
                visited.add(nei)
                return
            if nei not in visited and nei in potential:
                solution_1630_1_2(nei, curr + 1, v)
        for node in potential:
            solution_1630_1_2(node, 1, {})
        return self.ans