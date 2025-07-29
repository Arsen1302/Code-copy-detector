class Solution:
    def solution_1135_4(self, n: int) -> int:
        return int("".join(bin(i)[2:] for i in range(1, n+1)), 2) % 1_000_000_007