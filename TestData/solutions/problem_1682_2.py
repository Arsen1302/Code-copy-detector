class Solution:
    def solution_1682_2(self, a: int, b: int) -> int:
        count = 0
        c, d  = max(a,b), min(a,b)
        for x in range(1,c):
            if c % x == 0:
                if d % x == 0:
                    count += 1
        if a == b:
            count += 1
        return count