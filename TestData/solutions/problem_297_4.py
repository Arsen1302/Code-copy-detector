class Solution:
    @cache
    def solution_297_4(self, n: int) -> int:
        return n if n <= 1 else self.solution_297_4(n-1)+self.solution_297_4(n-2)