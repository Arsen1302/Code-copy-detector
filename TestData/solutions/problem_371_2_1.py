class Solution:
    def solution_371_2_1(self, equation: str) -> str:
        left, right = equation.split('=')
        def solution_371_2_2(s):
            x_cnt, c_cnt, cur, sign = 0, 0, '', 1
            for c in s + '+':             # adding `+` to process the last term of `s`, since sign is a trigger 
                if c in '-+':             # use sign as a trigger
                    if not cur:           # handle edge case: leading `-` (e.g. "-x=-1")
                        sign = -1 if s[0] == '-' else 1
                    elif cur[-1] == 'x':  # if `cur` is a term of `x`
                        x_cnt += sign * (int(cur[:-1]) if cur[:-1] else 1)
                    else:                 # if `cur` is a constant term
                        c_cnt += sign * int(cur)
                    sign, cur = 1 if c == '+' else -1, '' # get new `sign` &amp; reset `cur`
                else: cur += c            # other situation, append char to `cur`
            return x_cnt, c_cnt           # return #_of_x and #_of_constant 
        (x1, c1), (x2, c2) = solution_371_2_2(left), solution_371_2_2(right)
        if c2-c1 == x1-x2 == 0: return 'Infinite solutions'
        elif x1-x2 == 0: return 'No solution'
        else: return f'x={(c2-c1)//(x1-x2)}'