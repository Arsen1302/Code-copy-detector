class Solution:
	    def solution_1347_5(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        queue = [start]
        graph = {}
        for vertex in range(n):
            graph[vertex] = []
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = {start}
        
        while len(queue) != 0:
            node = queue.pop(0)
            if node == end:
                return True
            
            for vertex in graph[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
        
        return False