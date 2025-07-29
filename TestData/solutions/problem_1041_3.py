class Solution:
    def solution_1041_3(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if stack and stack[-1] == s[i].swapcase():
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(stack)