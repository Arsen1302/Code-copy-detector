class Solution:
    def solution_165_3(self, preorder: str) -> bool:
        stack = []
        for n in preorder.split(","):
            stack.append(n)
            while stack[-2:] == ["#", "#"]: 
                stack.pop()
                stack.pop()
                if not stack: return False 
                stack[-1] = "#"
        return stack == ["#"]