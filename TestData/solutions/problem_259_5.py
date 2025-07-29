class Solution:
    def solution_259_5(self, x: int, y: int) -> int:
        count = 0
        while x!= 0 or y!= 0:
            if ((x >> 1 << 1) != x and (y >> 1 << 1) == y) or  ((x >> 1 << 1) == x and (y >> 1 << 1) != y):
                count += 1
            x = x >> 1
            y = y >> 1
        return count