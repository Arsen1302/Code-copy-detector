class Solution:
    def solution_1508_5(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indeg, graph = [0]*n, defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
            
        queue, res = deque([i for i in range(n) if indeg[i] == 0]), [set() for _ in range(n)]
        
        while queue:
            curr = queue.popleft()

            for nxtNode in graph[curr]:
                res[nxtNode].add(curr)
                res[nxtNode] |= res[curr]
                        
                indeg[nxtNode] -= 1
                if indeg[nxtNode] == 0:
                    queue.append(nxtNode)
                        
        return list(map(sorted, res))