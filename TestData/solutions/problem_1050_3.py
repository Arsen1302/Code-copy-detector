class Solution:
    def solution_1050_3(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(set)
        
        visited = set()
        seen = set()
        
        for src,dest in edges:
            graph[src].add(dest)
            seen.add(dest)
        
        output = []
        for i in range(n):
            if i not in seen:
                output.append(i)
        
        return output