class Solution:
    def solution_293_4(self, num: int) -> str:
        if num < 0: return "-" + self.solution_293_4(-num)
        if num < 7: return str(num)    
        return self.solution_293_4(num//7) + str(num%7)