class Solution:
    def solution_1652_3(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        return "".join(stack)