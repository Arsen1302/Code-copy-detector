class Solution:
    def solution_434_5_1(self, left, right):
        return list(filter(self.solution_434_5_2, range(left,right+1)))
        
    def solution_434_5_2(self, num):
        digits = {int(c) for c in str(num)}
        if 0 in digits: return False
        else: return all(num % d == 0 for d in digits)