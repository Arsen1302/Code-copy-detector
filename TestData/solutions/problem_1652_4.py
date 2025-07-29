class Solution:
    def solution_1652_4(self, s: str) -> str:
        string = list(s)  
        stack = []
        for i in string:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)