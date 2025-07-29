class Solution:
    def solution_823_2(self, U: int, L: int, C: List[int]) -> List[List[int]]:
        M, u = [[0]*len(C) for _ in range(2)], C.count(2)
        if U + L != sum(C) or u > min(L,U): return []
        for j,s in enumerate(C):
            if s == 2: M[0][j] = M[1][j] = 1
        for j,s in enumerate(C):
            if s == 1:
                if u < U: M[0][j], u = 1, u + 1
                else: M[1][j] = 1
        return M
            
			
- Junaid Mansuri