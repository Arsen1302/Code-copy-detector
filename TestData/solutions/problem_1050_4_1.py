class Solution:
    def solution_1050_4_1(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        visited = set()
        result = set()
        
        for src,dest in edges:
            graph[src].add(dest)
            
        
        def solution_1050_4_2(src):
            visited.add(src)
            for dest in graph[src]:
                if dest not in visited:
                    solution_1050_4_2(dest)
                elif dest in result:
                    result.remove(dest)
                    
        
        for i in range(n):
            if i not in visited:
                result.add(i)
                solution_1050_4_2(i)
                
        return result