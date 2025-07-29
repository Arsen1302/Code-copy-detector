class Solution:
    def solution_718_2(self, A: List[int]) -> int:
    	SP, L = [[0]*50 for _ in range(50)], len(A)
    	for i in range(2,L):
    		for j in range(L-i):
    			s, e, SP[s][e] = j, j + i, math.inf
    			for k in range(s+1,e): SP[s][e] = min(SP[s][e], A[s]*A[k]*A[e] + SP[s][k] + SP[k][e])
    	return SP[0][L-1]
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com