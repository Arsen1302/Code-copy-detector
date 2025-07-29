class Solution:
    def solution_603_2(self, s: str) -> int:
        stack = []
        for c in s:
            if len(stack):
                if stack[-1] == '(' and c == ')':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)            
        return len(stack)