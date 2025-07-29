class Solution:
    def solution_441_4(self, T: List[int]) -> List[int]:
        res, stack = [0] * len(T), []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res