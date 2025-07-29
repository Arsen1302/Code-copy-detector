class Solution:
    def solution_462_4(self, arr: List[int]) -> int:
        stack = []
        for i, x in enumerate(arr): 
            most = x
            while stack and stack[-1] > x: most = max(most, stack.pop())
            stack.append(most)
        return len(stack)