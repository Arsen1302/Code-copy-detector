class Solution:
    def solution_1452_5(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True