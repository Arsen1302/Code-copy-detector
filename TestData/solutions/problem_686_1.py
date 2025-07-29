class Solution:
    def solution_686_1(self, N: int) -> int:
    	return N + ([1,2,2,-1][N % 4] if N > 4 else [0,0,0,3,3][N])