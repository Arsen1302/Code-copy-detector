class Solution:
    def solution_1182_5_1(self, adj: List[List[int]]) -> List[int]:
        ## RC ##
        ## APPROACH : GRAPH / DFS ##
        graph = collections.defaultdict(list)
        for u,v in adj:
            graph[u].append(v)
            graph[v].append(u)
        
        first = None
        for u in graph:
            if len(graph[u]) == 1:
                first = u
                break
        
        res = []
        visited = set()
        def solution_1182_5_2(node):
            if node in visited:
                return
            visited.add(node)
            res.append(node)
            for nei in graph[node]:
                solution_1182_5_2(nei)
        solution_1182_5_2(first)
        return res