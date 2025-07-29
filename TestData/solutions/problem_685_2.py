class Solution:
    def solution_685_2(self, A: List[int], K: int) -> int:
    	S, a = sum(A), sorted([i for i in A if i < 0])
    	L, b = len(a), min([i for i in A if i >= 0])
    	if L == 0: return S if K % 2 == 0 else S - 2*b
    	if K <= L or (K - L) % 2 == 0: return S - 2*sum(a[:min(K,L)])
    	return S - 2*sum(a[:-1]) if -a[-1] < b else S - 2*sum(a) - 2*b
		
		
- Junaid Mansuri