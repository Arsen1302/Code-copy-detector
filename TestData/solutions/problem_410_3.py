class Solution:
    def solution_410_3(self, n: int) -> bool:
        while n > 0:
            if not 3 > (n &amp; 3) > 0:
                return False
            n >>= 1
        return True