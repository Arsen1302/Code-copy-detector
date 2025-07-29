class Solution:
    def solution_397_4(self, nums: List[int]) -> int:
        stack = [nums[0]]
        ret = 1
        for i in range(1, len(nums)):
            if stack and stack[-1] >= nums[i]: stack.clear()
            stack.append(nums[i])
            ret = max(ret, len(stack))
        return ret