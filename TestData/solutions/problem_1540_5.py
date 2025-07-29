class Solution:
    def solution_1540_5(self, num1: int, num2: int) -> int:
        mask = 0xFFFFFFFF
        if num2 == 0:
            return num1 if num1 < 0x80000000 else ~(num1 ^ mask)
        carry = ((num1 &amp; num2) << 1) &amp; mask
        non_carry = (num1 ^ num2) &amp; mask
        return self.solution_1540_5(non_carry,carry)