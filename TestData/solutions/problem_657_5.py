class Solution:
    def solution_657_5(self, A: List[int]) -> int:
    	L, _ = len(A), A.sort()
    	for i in range(L-1,1,-1):
    		a = A[i]
    		for j in range(i-1,0,-1):
    			b, m, c = A[j], a - A[j] + 1, A[j-1]
    			if m > b: break
    			if c >= m: return a + b + c
    	return 0
		
		

- Junaid Mansuri
(LeetCode ID)@hotmail.com