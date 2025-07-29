class Solution:
    def solution_1599_1_1(self, n: int, edges: List[List[int]]) -> int:
        def solution_1599_1_2(graph,node,visited):
            visited.add(node)
            self.c += 1
            for child in graph[node]:
                if child not in visited:
                    solution_1599_1_2(graph, child, visited)
        
        #build graph
        graph = {}
        for i in range(n):
            graph[i] = []
            
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        count = 0
        totalNodes = 0
        
        #run solution_1599_1_2 in unvisited nodes
        for i in range(n):
            if i not in visited:
                self.c = 0
                solution_1599_1_2(graph, i, visited)
                
                count += totalNodes*self.c    # result 
                totalNodes += self.c          # total nodes visited 
        return count