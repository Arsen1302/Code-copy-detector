class Solution:
    def solution_1652_5(self, s: str) -> str: 
        stack=[]
        for i in s:
            if i=='*':
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)