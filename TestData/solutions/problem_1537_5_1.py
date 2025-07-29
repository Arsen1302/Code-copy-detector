class Solution:
    def solution_1537_5_1(self, expression: str) -> str:
        plus_index, n, ans = expression.find('+'), len(expression), [float(inf),expression] 
        def solution_1537_5_2(exps: str):
            return eval(exps.replace('(','*(').replace(')', ')*').lstrip('*').rstrip('*'))
        for l in range(plus_index):
            for r in range(plus_index+1, n):
                exps = f'{expression[:l]}({expression[l:plus_index]}+{expression[plus_index+1:r+1]}){expression[r+1:n]}'
                res = solution_1537_5_2(exps)
                if ans[0] > res:
                    ans[0], ans[1] = res, exps
        return ans[1]