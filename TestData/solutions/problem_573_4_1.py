class Solution:
    def solution_573_4_1(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = dict()
        for u, v in dislikes:
            graph.setdefault(u-1, []).append(v-1)
            graph.setdefault(v-1, []).append(u-1)
            
        def solution_573_4_2(n, i=1):
            """Return True if bipartite"""
            if seen[n]: return (i-seen[n])%2 == 0
            seen[n] = i
            return all(solution_573_4_2(nn, i+1) for nn in graph.get(n, []))
        
        seen = [0]*N
        return all(solution_573_4_2(n) for n in range(N) if not seen[n])