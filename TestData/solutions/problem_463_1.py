class Solution:
    def solution_463_1(self, arr: List[int]) -> int:
        stack = []
        
        for num in arr:
            lagest = num
            while stack and num < stack[-1]:
                lagest = max(lagest, stack.pop())

            stack.append(lagest)
        
        return len(stack)