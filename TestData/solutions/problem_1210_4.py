class Solution:
    def solution_1210_4(self, n: int) -> bool:
        while n: 
            n, r = divmod(n, 3)
            if r == 2: return False 
        return True