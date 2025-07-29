class Solution:
    def solution_1533_3_1(self, current: str, correct: str) -> int:
        def solution_1533_3_2(t):
            hh, mm = t.split(':')
            return int(hh) * 60 + int(mm)
        
        current, correct = solution_1533_3_2(current), solution_1533_3_2(correct)
        operations = 0
        diff = correct - current
        
        for mins in [60, 15, 5, 1]:
            quotient, remainder = divmod(diff, mins)
            operations += quotient
            diff = remainder
                
        return operations