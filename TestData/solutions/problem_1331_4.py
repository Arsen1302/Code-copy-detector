class Solution:
    def solution_1331_4(self, n: int) -> bool:
        c = 0
        for i in range(1,n+1):
            if n/i == int(n/i):
                c += 1
            if c>3:
                return False
        return c == 3