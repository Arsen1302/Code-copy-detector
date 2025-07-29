class Solution: 
    def solution_1652_1(self, s: str) -> str:
        stack = []
        for ch in s: 
            if ch == '*': stack.pop()
            else: stack.append(ch)
        return ''.join(stack)