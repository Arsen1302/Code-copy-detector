class Solution:
    def solution_837_2(self, n: int) -> int:
        return prod(list(map(int, str(n))))-sum(list(map(int, str(n))))