class Solution:
    def solution_792_5_1(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if not connections:
            return []
        
        def solution_792_5_2(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph
            
        graph = solution_792_5_2(connections)
        visited = [False for _ in range(n)]
        counter = 0
        id_low = defaultdict(dict)
        critical_connections = []
        
        def solution_792_5_3(node, parent):
            nonlocal graph, visited, counter, id_low, critical_connections
            if visited[node]:
                return
            visited[node] = True
            id_low[node]['id'] = counter
            id_low[node]['low'] = counter
            counter += 1
            for node2 in graph[node]:
                if node2 == parent:
                    continue
                solution_792_5_3(node2, node)
                if id_low[node]['id'] < id_low[node2]['low']:
                    critical_connections.append([node, node2])
                id_low[node]['low'] = min(id_low[node]['low'], id_low[node2]['low'])
        
        solution_792_5_3(0, -1)
        return critical_connections