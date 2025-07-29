class Solution:
    def solution_1180_3(self, n: int) -> int:
        a = 0
        b = 0
        s = 0
        while n > s:
            a += 1
            b += a
            s += b
        while n <= s:
            s -= a
            a -= 1
            b -= 1
        return b + 1