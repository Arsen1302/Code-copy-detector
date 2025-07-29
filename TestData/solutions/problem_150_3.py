class Solution:
    def solution_150_3(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        adj = defaultdict(list)
        edge_count = defaultdict(int)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            edge_count[a] += 1
            edge_count[b] += 1
            
        q = deque(n for n in adj if len(adj[n]) == 1)
        visited = set(q)
        
        while len(visited) < n:
            length = len(q)
            for _ in range(length):
                node = q.popleft()                
                for neighbor in adj[node]:
                    if  neighbor not in visited:
                        edge_count[neighbor] -= 1
                        if edge_count[neighbor] == 1:
                            q.append(neighbor)
                            visited.add(neighbor)
                       
        return q