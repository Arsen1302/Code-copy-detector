class Solution:
    def solution_402_3_1(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        
        def solution_402_3_2(i):
            if parents[i] != i:
                parents[i] = solution_402_3_2(parents[i])
            return parents[i]
            
        def solution_402_3_3(i,j):
            parents[i] = j
        
        for e in edges:
            e1 = solution_402_3_2(e[0])
            e2 = solution_402_3_2(e[1])
            if e1 == e2:
                return e
            solution_402_3_3(e1, e2)