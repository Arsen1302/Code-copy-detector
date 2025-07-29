class Solution:
    def solution_603_5(self, s: str) -> int:
        O, C = 0, 0
        for char in s:
            if char == '(':
                O += 1
            elif char == ')':
                if O > 0:
                    O -= 1
                else :
                    C += 1
        return O + C