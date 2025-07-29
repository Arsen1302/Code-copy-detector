class Solution:
    def solution_349_2_1(self, expression: str) -> str:
        pairs, cur, sign, multiple = [], '', 0, 1
        for c in expression+'+':
            if not sign:
                if c == '-': sign = -1
                else: sign, cur = 1, cur + c
            elif c in '-+':
                left, right = cur.split('/')
                pairs.append((abs(int(left)) * sign, abs(int(right))))
                multiple *= pairs[-1][1]
                sign, cur = -1 if c == '-' else 1, ''
            else: cur += c
        s = sum([n * multiple // d for n, d in pairs])
        def solution_349_2_2(a, b):
            while b: a, b = b, a % b
            return abs(a)                
        divisor = solution_349_2_2(s, multiple)
        return f'{s//divisor}/{multiple//divisor}'