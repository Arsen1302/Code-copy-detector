class Solution:
    def solution_573_3_1(self, n: int, dislikes: List[List[int]]) -> bool:
        def solution_573_3_2(n: int, pairs: List[List[int]]):
            graph = []
            for i in range(n):
                graph.append([])
            for pair in pairs:
                personA = pair[0] - 1
                personB = pair[1] - 1
                graph[personA].append(personB)
                graph[personB].append(personA)
            return graph
        
        graph = solution_573_3_2(n, dislikes)
        
        visited = [False] * n
        marked = [False] * n
        
        def solution_573_3_3(cur):
            visited[cur] = True
            for neighbor in graph[cur]:
                if visited[neighbor]:
                    if marked[neighbor] == marked[cur]:
                        return False
                else:
                    marked[neighbor] = not marked[cur]
                    solution_573_3_3(neighbor)
        
        for i in range(n):
            if not visited[i]:
                if False == solution_573_3_3(i):
                    return False
        
        return True