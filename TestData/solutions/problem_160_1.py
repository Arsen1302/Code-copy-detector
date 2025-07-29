class Solution:
    def solution_160_1(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        else:
            return n % 3 == 0 and self.solution_160_1(n // 3)