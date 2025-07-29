class Solution:
    def solution_259_3(self, x: int, y: int) -> int:
        diff = x^y
        res = 0
        while diff:
            res+= diff&amp;1
            diff>>=1
        return res