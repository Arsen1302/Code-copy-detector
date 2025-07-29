class Solution:
    def solution_755_4(self, P: str) -> List[int]:
        D, A, v = {'(':1, ')':-1}, [], 0
        for p in P:
            if v*D[p] > 0:
                v -= D[p]
                A.append(0)
            else:
                v += D[p]
                A.append(1)
        return A
		
		
- Junaid Mansuri
- Chicago, IL