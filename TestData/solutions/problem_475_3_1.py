class Solution:
    def solution_475_3_1(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        
        def solution_475_3_2(i, color):
            colors[i] = color
            for node in graph[i]:
                if colors[node] == color: 
                    return False    
                elif colors[node] < 0 and not solution_475_3_2(node, 1 - color):
                    return False
            return True    
        
        for i in range(n):
            if colors[i] < 0 and not solution_475_3_2(i, 0):
                return False
        return True