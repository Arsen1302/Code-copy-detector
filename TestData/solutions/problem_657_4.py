class Solution:
    def solution_657_4(self, A: List[int]) -> int:
    	L, _ = len(A), A.sort()
    	for i in range(L-1,1,-1):
    		if A[i] < A[i-1] + A[i-2]: return sum(A[i-2:i+1])
    	return 0