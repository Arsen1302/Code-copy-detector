class Solution:
    def solution_853_5(self, A: List[int], t: int) -> int:
        L, A, y = len(A), [0]+sorted(A), 0
        for i in range(L):
            y += (A[i+1]-A[i])*(L-i)
            if y >= t: return round(A[i+1] + (t-y)/(L-i) - 0.01)
			
			
- Junaid Mansuri
- Chicago, IL