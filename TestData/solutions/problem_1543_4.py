class Solution:
    def solution_1543_4(self, total: int, cost1: int, cost2: int) -> int:
        c, C = sorted((cost1, cost2))
        return sum((total - i * C) // c + 1 for i in range(total // C + 1))