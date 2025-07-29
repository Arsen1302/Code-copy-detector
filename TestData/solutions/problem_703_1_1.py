class Solution:
    def solution_703_1_1(self, queries: List[str], pattern: str) -> List[bool]:
        
        def solution_703_1_2(p, q):
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == q[j]: i += 1
                elif q[j].isupper(): return False
            return i == len(p)
        
        return [True if solution_703_1_2(pattern, s) else False for s in queries]