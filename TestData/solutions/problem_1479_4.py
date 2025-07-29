class Solution:
    def solution_1479_4(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0 
        for k in range(n, -1, -1): 
            for good in combinations(list(range(n)), k): 
                cand = True 
                for i in good: 
                    if cand: 
                        for j in range(n): 
                            if i != j and (statements[i][j] == 0 and j in good or statements[i][j] == 1 and j not in good): 
                                cand = False 
                                break 
                if cand: return k