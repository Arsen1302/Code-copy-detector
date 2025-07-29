class Solution:
    def solution_751_4(self, expression: str) -> bool:
        d_val = {'t': True, 'f': False}
        d_reverse_val = {True: 't', False: 'f'}
        
        stack = []
        
        for exp in expression:
            if exp == ')':
                args = []
                while stack[-1] != '(':
                    args.append(stack.pop())
                
                # pop (
                stack.pop()
                # pop operation
                op = stack.pop()
                 
                if op == '!':
                    stack.append(d_reverse_val[not d_val[args[0]]])
                
                if op == '&amp;':
                    val = d_val[args[0]]
                    for arg in args[1:]:
                        val = val and d_val[arg]
                    stack.append(d_reverse_val[val])
                
                if op == '|':
                    val = d_val[args[0]]
                    for arg in args[1:]:
                        val = val or d_val[arg]
                    stack.append(d_reverse_val[val])
            elif exp != ',':
                stack.append(exp)
        
        
        return d_val[stack[0]]