class Solution:
    def solution_1331_2(self, n: int) -> bool:
        if n == 1: return False # edge case 
        
        x = int(sqrt(n))
        if x*x != n: return False 
        
        for i in range(2, int(sqrt(x))+1): 
            if x % i == 0: return False 
        return True