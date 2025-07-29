class Solution:
    def solution_683_3(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == 'c' and len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        
        if ''.join(stack) == 'abc': stack = []
            
        return stack == []