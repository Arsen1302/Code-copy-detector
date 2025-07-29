class Solution:
    def solution_573_5(self, n: int, dislikes: List[List[int]]) -> bool:
        res = True
        visited = [0] * n
        groups = [-1] * n
        graph = [[] for _ in range(n)]
        # store the edges
        for i,j in dislikes:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        
        for v in range(n):
            if visited[v] == 0:
                q = []
                visited[v] = 1
                groups[v] = 0
                q.append(v)
                while q and res:
                    cur = q.pop(0)
                    for nei in graph[cur]:
                        if visited[nei] == 0:
                            groups[nei] = 1 if groups[cur] != 1 else 0
                            visited[nei] = 1
                            q.append(nei)
                        else:
                            if groups[nei] == groups[cur]:
                                res = False                
                
        return res