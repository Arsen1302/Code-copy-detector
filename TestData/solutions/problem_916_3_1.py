class Solution:
    def solution_916_3_1(self, node, target, t, prob):
        self.visited.add(node)
        if t == 0:
            return prob if node == target else 0.0
        children = set()
        for v in self.graph[node]:
            if v not in self.visited:
                children.add(v)
        if not children:
            return prob if node == target else 0.0
        for v in children:
            p = self.solution_916_3_1(v, target, t-1, prob / len(children))
            if p > 0:
                return p
        return 0.0
    
    def solution_916_3_2(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        self.graph = defaultdict(set)
        for v, u in edges:
            self.graph[v].add(u)
            self.graph[u].add(v)
        self.visited = set()
        return self.solution_916_3_1(1, target, t, 1.0)