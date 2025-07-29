class Solution:
    def solution_113_3_1(self, s: str) -> int:

        def solution_113_3_2():
            terminate = {'+', '-', '|'}

            term, sign = None, None
            cur = ''

            for ch in s + '|':
                if ch == ' ': continue
                
                if ch.isdigit():
                    cur += ch
                    continue

                if sign:
                    if sign == '*':
                        term *= int(cur)
                    else:
                        term //= int(cur)
                else:
                    term = int(cur)
                
                sign = ch
                
                if ch in terminate:
                    yield (term, ch)
                    term, sign = None, None
                
                cur = ''
                
        res = 0
        prevSign = None
        
        for term, sign in solution_113_3_2():
            if not prevSign or prevSign == '+':
                res += term
            else:
                res -= term

            prevSign = sign
            
        return res