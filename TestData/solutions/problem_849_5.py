class Solution:
    def solution_849_5(self, N: List[int], k: int) -> bool:
        L, C = len(N), collections.Counter(N)
        for i in range(L//k):
            m = min(C.keys())
            for j in range(m,m+k):
                if C[j] > 1: C[j] -= 1
                else: del C[j]
        return not (C or L % k)
		
		
- Junaid Mansuri
- Chicago, IL