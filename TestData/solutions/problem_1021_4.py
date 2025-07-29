class Solution:
    def solution_1021_4(self, a: int, b: int) -> int:
        empty = 0
        count = 0
        while a > 0:
            count += a
            empty += a
            a = empty // b
            empty %= b
        return count