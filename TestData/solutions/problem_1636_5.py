class Solution(object):
    def solution_1636_5(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        
        restricted = set(restricted)
        adj_list = {i: [] for i in range(n)}
        for (u, v) in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        stack = [0]
        n_reachable = 1
        visited = set([])
        
        while len(stack) > 0:
            u = stack.pop(0)
            visited.add(u)
            done_edges = []
            for v in adj_list[u]:
                if v not in visited and v not in restricted:
                    stack.append(v)
                    n_reachable += 1
                    
        return n_reachable