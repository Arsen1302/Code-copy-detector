class Solution:
    def solution_210_4_1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def solution_210_4_2():
            graph = defaultdict(dict)
            for (a, b), v in zip(equations, values):    # zip into two tuples
                graph[a][b] = v
                graph[b][a] = 1/v
            return graph
    
        graph = solution_210_4_2()                            # build given relationship
        
                                                        # build all other relationship using floyd
        for k in graph:                                 # k: intermediate vertext
            for i in graph:
                for j in graph:                         # i, j : one matrix at a time
                    if k in graph[i] and j in graph[k]:
                        graph[i][j] = graph[i][k] * graph[k][j]
        
        return [graph[a][b] if b in graph[a] else -1.00000 for a, b in queries]