class Solution:
    def solution_1599_5_1(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def solution_1599_5_2(p): 
            if parent[p] != p: parent[p] = solution_1599_5_2(parent[p])
            return parent[p]
        
        for p, q in edges: 
            prt, qrt = solution_1599_5_2(p), solution_1599_5_2(q)
            if prt != qrt: parent[prt] = qrt
        
        freq = Counter(solution_1599_5_2(p) for p in range(n))
        return sum(v*(n-v) for v in freq.values())//2