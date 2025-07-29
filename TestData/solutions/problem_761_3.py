class Solution:
    def solution_761_3(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # shortest = BFS 
        # there can be cycles so alternating paths after a cycle can be different
        # tracking visited is not just about the node, also includes the colors
        from collections import defaultdict
        
        g = defaultdict(list)
        
        for a, b in redEdges:
            g[a].append((b, 'red'))
        for u, v in blueEdges:
            g[u].append((v, 'blue'))
            
        answer = [-1 for _ in range(n)]
        
        from collections import deque 
        q = deque([(0, 'red', 0), (0, 'blue', 0)]) # can start from either blue or red. represents node, color, dist
        visited = set() # track the nodes we've visited so we don't hit a cycle
        
        # init visited and answer of first node!
        visited.add((0, 'red'))
        visited.add((0, 'blue'))
        answer[0] = 0
        
        while q:
            node, color, dist = q.popleft()         
            
            for nei, neicolor in g[node]:
                if (nei, neicolor) in visited or color == neicolor:
                    continue
                
                if answer[nei] < 0:
                    answer[nei] = dist + 1
                q.append((nei, neicolor, dist + 1))
                visited.add((nei, neicolor))
                
        return answer