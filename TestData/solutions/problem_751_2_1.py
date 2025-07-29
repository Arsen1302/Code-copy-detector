class Solution:
    def solution_751_2_1(self, expression: str) -> bool:
        logics = []
        stack = []
        
        def solution_751_2_2(tmp, top, op):
            if op == '!':
                tmp = 't' if tmp == 'f' else 'f'
            elif op == '&amp;':
                tmp = 't' if (tmp == 't' and top == 't') else 'f'
            elif op == '|':
                tmp = 't' if (tmp == 't' or top == 't') else 'f'
            return tmp

        for i in expression:
            if i in ('!', '&amp;', '|'):
                logics.append(i)
            elif i == ')':
                op = logics.pop()
                tmp = stack.pop()
                while stack:
                    top = stack.pop()
                    # print(tmp, top, op)
                    if op == '!' and top == '(': tmp = solution_751_2_2(tmp, tmp, op)
                    if top == '(': break
                    tmp = solution_751_2_2(tmp, top, op)
                stack.append(tmp)
            elif i == ',': continue
            else:
                stack.append(i)
            # print(stack, logics, i)
        
        if logics:
            op = logics.pop()
            tmp = stack.pop()
            while stack:
                top = stack.pop()
                tmp = solution_751_2_2(tmp, top, op)
            stack.append(tmp)
        
        return True if stack[0] == 't' else False
        
                    
# Time: O(N)
# Space: O(N)