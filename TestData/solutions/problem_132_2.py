class Solution:
    def solution_132_2(self, n: int) -> int:
    	N, I = [1], {2:0, 3:0, 5:0}
    	for _ in range(n-1):
    		I = {i:bisect.bisect(N, N[-1]//i, I[i]) for i in [2,3,5]}
    		N.append(min(N[I[2]]*2,N[I[3]]*3,N[I[5]]*5))
    	return N[-1]