class Solution:
    def solution_1016_3_1(self, n: int) -> bool:
        
        @cache
        def solution_1016_3_2(x): 
            if x == 0: return False 
            for k in range(1, int(sqrt(x))+1):
                if not solution_1016_3_2(x-k*k): return True 
            return False 
        
        return solution_1016_3_2(n)