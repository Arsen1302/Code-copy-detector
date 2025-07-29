class Solution:
    def solution_790_5(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ")":
                stack.append(char)
                continue
            
            current = []
            while stack[-1] != "(":
                current.append(stack.pop())
            
            stack.pop()
            
            stack += current
        
        return "".join(stack)