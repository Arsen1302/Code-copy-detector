class Solution:
    def solution_262_2(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        return desiredTotal == 0 or desiredTotal % (maxChoosableInteger + 1)