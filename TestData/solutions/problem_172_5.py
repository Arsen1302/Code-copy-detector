class Solution:
    def solution_172_5(self, num: int) -> bool:
        if num <= 0: return False
        while num:
            num, r = divmod(num, 4)
            if num and r: return False 
        return r == 1