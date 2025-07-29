class Solution:
    def solution_718_1_1(self, A: List[int]) -> int:
    	SP, LA = [[0]*50 for i in range(50)], len(A)
    	def solution_718_1_2(a,b):
    		L, m = b - a + 1, math.inf; 
    		if SP[a][b] != 0 or L < 3: return SP[a][b]
    		for i in range(a+1,b): m = min(m, A[a]*A[i]*A[b] + solution_718_1_2(a,i) + solution_718_1_2(i,b))
    		SP[a][b] = m; return SP[a][b]
    	return solution_718_1_2(0,LA-1)