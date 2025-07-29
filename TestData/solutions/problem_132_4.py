class Solution:
    def solution_132_4(self, n: int) -> int:
    	N, p, I = [1], [2,3,5], [0]*3
    	for _ in range(n-1):
    		N.append(min([N[I[i]]*p[i] for i in range(3)]))
    		for i in range(3): I[i] += N[I[i]]*p[i] == N[-1]
    	return N[-1]
		
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com