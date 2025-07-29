class Solution:
    def solution_1498_1(self, num: int) -> int:
        return num // 2 if sum([int(k) for k in str(num)]) % 2 == 0 else (num - 1) // 2