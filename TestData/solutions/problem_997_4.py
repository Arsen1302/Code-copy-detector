class Solution:
    def solution_997_4(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            xor = xor ^ start
            start+=2
        return xor