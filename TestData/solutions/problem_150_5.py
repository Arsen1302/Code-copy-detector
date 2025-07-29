class Solution:
    def solution_150_5(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        for u, v in edges: 
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        
        while n > 2: 
            n -= len(leaves)
            newl = []
            for u in leaves: 
                v = graph[u].pop()
                graph[v].remove(u)
                if len(graph[v]) == 1: newl.append(v)
            leaves = newl
        return leaves