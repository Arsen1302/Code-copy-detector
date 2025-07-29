class Solution:
    def solution_160_5(self, n: int) -> bool:
        if n <= 0: return False 
        while n:
            n, r = divmod(n, 3)
            if n and r: return False 
        return r == 1