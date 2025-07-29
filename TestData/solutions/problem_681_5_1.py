class Solution:
    from collections import defaultdict
    from itertools import product
    def solution_681_5_1(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = defaultdict(int)
        cols = defaultdict(int)
        downright = defaultdict(int)
        downleft = defaultdict(int)
        lampset = set(map(tuple, lamps))
        
        def solution_681_5_2(r, c, k):
            rows[r] += k
            cols[c] += k
            downright[c - r] += k
            downleft[c + r] += k
        
        def solution_681_5_3(r, c):
            return rows[r] > 0 or cols[c] > 0 or downright[c - r] > 0 or downleft[c + r] > 0
        
        for r, c in lampset:
            solution_681_5_2(r, c, 1)
            
        res = []
        
        for r, c in queries:
            res.append(int(solution_681_5_3(r, c)))
            for pos in product(range(r - 1, r + 2), range(c - 1, c + 2)):
                if pos in lampset:
                    lampset.remove(pos)
                    solution_681_5_2(pos[0], pos[1], -1)
                    
        return res