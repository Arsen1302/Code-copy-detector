class Solution:
    def solution_111_4(self, s: str) -> int:
        #pre-processing to tokenize input 
        s = s.replace(" ", "") #remote white space 
        
        tokens = [] #collect tokens
        lo = hi = 0
        while hi <= len(s):
            if hi == len(s) or s[hi] in "+-()": 
                if lo < hi: tokens.append(s[lo:hi])
                if hi < len(s): tokens.append(s[hi])
                lo = hi + 1
            hi += 1
        
        #Dijkstra's two-stack algo
        opd, opr = [], [] #operand &amp; operator stacks
        for token in tokens: 
            if token in "+-(": opr.append(token)
            else:
                if token == ")": 
                    opr.pop()
                    token = opd.pop()
                else:
                    token = int(token)
                if opr and opr[-1] != "(":
                    op = opr.pop()
                    x = opd.pop()
                    if op == "+": token = x + token
                    else: token = x - token
                opd.append(token)
        return opd[-1]