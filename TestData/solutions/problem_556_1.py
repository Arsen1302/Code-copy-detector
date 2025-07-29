class Solution:
    def solution_556_1(self, n: int) -> bool:
        for i in range(32):
            if Counter(str(n))==Counter(str(2**i)):
                return True
        return False