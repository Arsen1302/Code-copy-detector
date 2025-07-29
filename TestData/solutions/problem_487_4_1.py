class Solution:
    def solution_487_4_1(self, graph: List[List[int]]) -> List[List[int]]:
        
        def solution_487_4_2(path: List[int]):
            if path[-1] == len(graph) - 1:
                yield path
            else:
                for v in graph[path[-1]]:
                    yield from solution_487_4_2(path + [v])
                
        return list(solution_487_4_2([0]))