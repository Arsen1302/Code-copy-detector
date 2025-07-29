class Solution:
    def solution_739_1(self, s: str) -> str:
        loc = {x: i for i, x in enumerate(s)}
        stack = []
        for i, x in enumerate(s): 
            if x not in stack: 
                while stack and x < stack[-1] and i < loc[stack[-1]]: stack.pop()
                stack.append(x)
        return "".join(stack)