class Solution:
    def solution_1210_1(self, n: int) -> bool:
        while n:
            n, rem = divmod(n, 3)
            if rem == 2:
                return False
        return True