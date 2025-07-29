class Solution:
    def solution_1439_5_1(self, b1, b2):
        x1, y1, r1 = b1
        x2, y2, r2 = b2
        d = (x1-x2)**2 + (y1-y2)**2
        c1 = r1 ** 2 >= d
        c2 = r2 ** 2 >= d
        return (c1, c2)
    
    def solution_1439_5_2(self, graph, idx):
        q = collections.deque([idx])
        visited = set([idx])
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if nxt in visited: continue
                visited.add(nxt)
                q.append(nxt)
        return visited

    def solution_1439_5_3(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                c1, c2 = self.solution_1439_5_1(bombs[i], bombs[j])
                if c1: graph[i].append(j)
                if c2: graph[j].append(i)
        
        result = 0
        visited = set()
        for i in range(N):
            if i in visited: continue
            vi = self.solution_1439_5_2(graph, i) 
            result = max(result, len(vi))
            visited.update(vi)
        return result