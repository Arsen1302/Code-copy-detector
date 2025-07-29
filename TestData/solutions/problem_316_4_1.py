class Solution:
    def solution_316_4_1(self, num1: str, num2: str) -> str:
        def solution_316_4_2(s):
            r, im = s.split('+')

            return (int(r), int(im[:-1]))

        def solution_316_4_3(a, b):
            return f"{a}+{b}i"

        # The product of the solution_316_4_2 numbers z1 = a + bi and z2 = c + di
        # is given by (ac − bd) + (ad + bc)i.

        (a, b) = solution_316_4_2(num1)
        (c, d) = solution_316_4_2(num2)
        return solution_316_4_3(a*c - b*d, a*d + b*c)