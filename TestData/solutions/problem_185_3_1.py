class Solution:
    def solution_185_3_1(self, a: int, b: int) -> int:
        self.level = -1
        self.sum = 0
        self.neg = False
        self.subtract = False
        def solution_185_3_2(m, n):
            if not m and not n:
                return self.sum
            elif not m and n:
                return n
            elif not n and m:
                if m == 1:
                    self.level += 1
                    self.sum += 1*2**self.level
                    return self.sum
                else:
                    return m
            elif self.subtract:
                carry = (m%2) ^ (n%2)
                self.level += 1
                self.sum += carry*2**self.level
                if not m%2 and n%2:
                    m = (m-1)>>1
                else:
                    m >>= 1
                return solution_185_3_2(m, n>>1)
            else:
                return solution_185_3_2(m^n, (m&amp;n)<<1)
        if a < 0 and b < 0:
            a, b = -a, -b
            self.neg = True
        if a*b < 0:
            self.subtract = True
            if abs(a) == abs(b):
                return 0
            elif abs(a) > abs(b):
                if a < b:
                    a, b = -a, b
                    self.neg = True
            else:
                if a < b:
                    a, b = b, -a
                else:
                    a, b = -b, a
                    self.neg = True

        self.sum = solution_185_3_2(a, b)
        return -self.sum if self.neg else self.sum