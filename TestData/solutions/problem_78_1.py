class Solution:
    def solution_78_1(self, n: int) -> int:
        quotient = n // 5
        return quotient + self.solution_78_1(quotient) if quotient >= 5 else quotient