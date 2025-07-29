class Solution:
    def solution_1303_2(self, s: str, part: str) -> str:
        stack = []
        for ch in s: 
            stack.append(ch)
            if "".join(stack[-len(part):]) == part: 
                for _ in range(len(part)): stack.pop()
        return "".join(stack)