class Solution:
    def solution_870_3_1(self, comp, idx, visited, graph):
        visited[idx] = True
        comp.append(idx)
        
        for neighbour in graph[idx]:
            if visited[neighbour] is False:
                comp = self.solution_870_3_1(comp, neighbour, visited, graph)
        
        return comp
                
        
    def solution_870_3_2(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
            
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
            
        totalEdges = 0
        for key, value in graph.items():
            totalEdges += len(value)
        
        totalEdges = totalEdges//2
        
        visited = [False]*n
        connectedComponents = []
        
        for i in range(n):
            if len(graph[i]) > 0 and visited[i] is False:
                component = []
                connectedComponents.append(self.solution_870_3_1(component, i, visited, graph))
            
            elif len(graph[i]) == 0:
                connectedComponents.append([i])
                
        totalComponents = len(connectedComponents)
        
        redundantEdges = totalEdges - ((n - 1) - (totalComponents - 1)) 
        
        requiredEdges = totalComponents - 1
        
        if redundantEdges >= requiredEdges:
            return requiredEdges
        else:
            return -1