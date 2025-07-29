class Solution:
    def solution_751_5(self, expression: str) -> bool:
        t = f = 0 
        operators, operands = [], []
        for x in expression: 
            if x in "!&amp;|": # operator 
                operators.append(x)
                operands.append([t, f])
                t = f = 0 
            elif x == "t": t += 1
            elif x == "f": f += 1
            elif x == ")": 
                op = operators.pop()
                if op == "!" and t or op == "&amp;" and f or op == "|" and not t: t, f = 0, 1
                else: t, f = 1, 0
                tt, ff = operands.pop()
                t, f = t+tt, f+ff
        return t