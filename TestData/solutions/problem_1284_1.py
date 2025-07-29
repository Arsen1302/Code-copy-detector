class Solution:
    @cache
    def solution_1284_1(self, n: int) -> int:
        return min((1 + max(i - 1, self.solution_1284_1(n - i)) for i in range (1, n)), default = 1)