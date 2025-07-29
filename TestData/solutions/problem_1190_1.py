class Solution:
    def solution_1190_1(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted((a, b, c))
        if a + b < c: return a + b
        return (a + b + c)//2