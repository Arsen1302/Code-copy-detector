class Solution:
    def solution_440_2(self, n: int) -> int:
    	N = [int(i) for i in str(n)]
    	L = len(N)
    	for I in range(L-1):
    		if N[I] > N[I+1]: break
    	if N[I] <= N[I+1]: return n
    	N[I+1:], N[I] = [9]*(L-I-1), N[I] - 1
    	for i in range(I,0,-1):
    		if N[i] >= N[i-1]: break
    		N[i], N[i-1] = 9, N[i-1] - 1
    	return sum([N[i]*10**(L-i-1) for i in range(L)])
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com