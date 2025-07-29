class Solution:
    def solution_1682_3(self, a: int, b: int) -> int:
        return sum(a % n == 0 and b % n == 0 for n in range(1, min(a, b) + 1))