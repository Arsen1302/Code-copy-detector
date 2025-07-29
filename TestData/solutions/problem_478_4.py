class Solution:
    def solution_478_4(self, N: int) -> int:
    	N, t, c = str(N), 0, 1
    	L, a, b = len(N) - 1, [1,2,3,3,3,4,5,5,6,7], [1,2,2,2,2,2,2,2,3,3] 
    	
    	for i in range(L):
    		if N[i] == '0': continue
    		t += a[int(N[i])-1]*7**(L-i) - c*b[int(N[i])-1]*3**(L-i)
    		if N[i] in '347': return t
    		if N[i] not in '18': c = 0
    	return t + a[int(N[-1])] - c*b[int(N[-1])]
		
		
- Junaid Mansuri