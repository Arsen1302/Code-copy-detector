class Solution:
    
    def solution_469_1(self, N: int, K: int) -> int:
        if N == 1: 
            return 0
        half = 2**(N - 2) 
        
        if K > half:
            return 1 if self.solution_469_1(N - 1, K - half) == 0 else 0
        else:
            return self.solution_469_1(N - 1, K)