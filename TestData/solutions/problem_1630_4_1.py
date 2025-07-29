class Solution:
    def solution_1630_4_1(self, edges: List[int]) -> int:
        N = len(edges)
        
        def solution_1630_4_2(node, step):
            if node in total:
                return total[node]
            if node in visited:
                return step-visited[node]
            else:
                visited[node] = step
                next_node = edges[node]
                if next_node == -1:
                    return -1
                return solution_1630_4_2(next_node, step+1)
                
        
        total = defaultdict(int)
        for e in range(len(edges)):
            if e not in total:
                visited = defaultdict(int)
                res = solution_1630_4_2(e, 0)
                for v in visited:
                    total[v] = res
                    
        ans = max(total.values())
        return -1 if ans == 0 else ans