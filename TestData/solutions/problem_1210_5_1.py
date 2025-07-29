class Solution:
    def solution_1210_5_1(self, n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))
        
    def solution_1210_5_2(self, n: int) -> bool:
        if n == 0 : 
            return False 
        else : 
            if '2' in self.solution_1210_5_1(n) : 
                return False 
            return True