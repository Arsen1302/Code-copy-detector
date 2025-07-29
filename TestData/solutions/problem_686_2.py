class Solution:
    def solution_686_2(self, N: int) -> int:
    	return eval(str(N)+''.join([['*','//','+','-'][(N-i-1)%4]+str(i) for i in range(N-1,0,-1)]))