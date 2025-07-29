class Solution:
    def solution_1218_5(self, edges: List[List[int]]) -> int:
        freq = {}
        for u, v in edges: 
            freq[u] = 1 + freq.get(u, 0)
            freq[v] = 1 + freq.get(v, 0)
        return next(k for k, v in freq.items() if v > 1)