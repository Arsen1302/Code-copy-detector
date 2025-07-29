class Solution:
    def solution_1613_5(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = [(0, -1)]
        for i, v in enumerate(nums):
            while len(stack) > 1 and v <= stack[-1][0]:
                if stack[-1][0] > threshold / (i - 1 - stack[-2][1]):
                    return i - 1 - stack[-2][1]
                stack.pop()
            stack.append((v, i))
        return -1