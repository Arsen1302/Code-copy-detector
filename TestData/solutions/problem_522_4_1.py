class Solution:
    def solution_522_4_1(self, v):
        self.visited.add(v)
        self.results[v] = [0, 0]
        for u in self.graph[v]:
            if u not in self.visited:
                self.solution_522_4_1(u)
                self.results[v][1] += self.results[u][1] + (self.results[u][0] + 1)
                self.results[v][0] += self.results[u][0] + 1
                
    def solution_522_4_2(self, v, parent):
        self.visited.add(v)
        if parent != -1:
            self.results[v][1] += self.results[parent][1] - (self.results[v][1] + self.results[v][0] + 1) + (
                self.results[parent][0] - (self.results[v][0] + 1) + 1)
            self.results[v][0] += self.results[parent][0] - (self.results[v][0] + 1) + 1
        for u in self.graph[v]:
            if u not in self.visited:
                self.solution_522_4_2(u, v)
                
    def solution_522_4_3(self, n: int, edges: List[List[int]]) -> List[int]:
        self.results = defaultdict(int)
        self.graph = defaultdict(set)
        for v, u in edges:
            self.graph[v].add(u)
            self.graph[u].add(v)
        self.visited = set()
        self.solution_522_4_1(0)
        self.visited = set()
        self.solution_522_4_2(0, -1)
        return [self.results[k][1] for k in range(n)]