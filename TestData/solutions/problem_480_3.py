class Solution:
    def solution_480_3(self, n: int) -> int:
        full_0, full_1, incomp_1 = 1, 2, 2
        for i in range(2, n):
            full_0, full_1, incomp_1 = full_1, full_0 + full_1 + incomp_1, 2 * full_0 + incomp_1
        return full_1 % (10 ** 9 + 7) if n >= 2 else 1