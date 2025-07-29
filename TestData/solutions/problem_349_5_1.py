class Solution:
    def solution_349_5_1(self, expression: str) -> str:

        def solution_349_5_2(s):
            sign = 1
            if s[0] == '-':
                s = s[1:]
                sign = -1
            
            (n, d) = s.split('/')

            return Rational(sign*int(n), int(d))

        ans = Rational(0,1)
        n = len(expression)
        op = Rational.solution_349_5_5
        i = 0
        while i < n:
            j = i + 1
            while j < n and expression[j] != '+' and expression[j] != '-':
                j += 1

            rat = solution_349_5_2(expression[i:j])
            ans = op(ans, rat)

            if j < n:
                if expression[j] == '+':
                    op = Rational.solution_349_5_5
                else:
                    op = Rational.solution_349_5_6

            i = j + 1

        return str(ans)

class Rational:
    # We represent a rational number as a pair (a, b) such that
    # a is an integer, b is a natural number and solution_349_5_9(a, b) = 1.
    def solution_349_5_3 (self, a: int, b: int):
        assert b != 0

        aa = abs(a)
        bb = abs(b)
        d = solution_349_5_9(aa, bb)
        
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            self.a = -1 * (aa // d)
        else:
            self.a = aa // d

        self.b = bb // d

    def solution_349_5_4(self):
        return f"{self.a}/{self.b}"

    def solution_349_5_5 (self, r):
        return Rational(self.a*r.b + self.b*r.a, self.b*r.b)

    def solution_349_5_6 (self, r):
        return Rational(self.a*r.b - self.b*r.a, self.b*r.b)

    def solution_349_5_7 (self, r):
        return self.a == r.a and self.b == r.b
    def solution_349_5_8 (self, r):
        return self.a != r.a or self.b != r.b

    def solution_349_5_9(self, c, d):
        if d == 0:
            return c

        return solution_349_5_9(d, c % d)