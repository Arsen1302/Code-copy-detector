class Solution:
    def solution_1347_4_1(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        
        graph = {}
        for vertex in range(n):
            graph[vertex] = []
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        visited = {start}
        
        for edge in graph[start]:
            if edge not in visited:
                result = self.solution_1347_4_2(edge, visited, graph, end)
                if result:
                    return True
        
        return False
    
    def solution_1347_4_2(self, node, visited, graph, end):
        if node == end:
            return True
        
        if node not in visited:
            visited.add(node)
            for edge in graph[node]:
                result = self.solution_1347_4_2(edge, visited, graph, end)
                if result:
                    return True