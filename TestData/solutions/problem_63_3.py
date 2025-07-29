class Solution:
    def solution_63_3(self, tokens) -> int:
        stack = [] 
        for ch in tokens:
                if ch == '+':
                    op1,op2 = stack.pop(), stack.pop()
                    stack.append(op2 + op1)
                elif ch == '-':
                    op1,op2 = stack.pop(), stack.pop()
                    stack.append(op2 - op1)
                elif ch == '*':
                    op1,op2 = stack.pop(), stack.pop()
                    stack.append(op2 * op1)
                elif ch == '/':
                    op1,op2 = stack.pop(), stack.pop()
                    # note // operator works as math.floor so if u divide 6// -132 = -1 
                    stack.append(int(op2 / op1))
                else:
                    stack.append(int(ch))
        
        return stack.pop()