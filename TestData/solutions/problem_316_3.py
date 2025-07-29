class Solution:
    def solution_316_3(self, num1: str, num2: str) -> str:
        ax, ay = map(int, num1.rstrip('i').split('+'))
        bx, by = map(int, num2.rstrip('i').split('+'))
        return '{x}+{y}i'.format(x = ax*bx - ay*by, y = ax*by + bx*ay)