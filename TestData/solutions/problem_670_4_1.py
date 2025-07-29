class Solution:
    def solution_670_4_1(self, equations: List[str]) -> bool:
        roots, get = [i for i in range(26)], lambda x: ord(x) - ord('a')
        
        def solution_670_4_2(x):
            return x if roots[x] == x else solution_670_4_2(roots[x])
        
        for a,op,_,b in equations:
            if op == '=':
                roots[solution_670_4_2(get(a))] = solution_670_4_2(get(b))
        
        for a,op,_,b in equations:
            if op == '!' and solution_670_4_2(get(a)) == solution_670_4_2(get(b)): return False
        return True