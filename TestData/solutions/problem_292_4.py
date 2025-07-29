class Solution(object):
    def solution_292_4(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1 for _ in range(n)]
        nums = nums + nums # Add another nums to simulate the circulate situation
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            if i < n:
                stack.append(i)
            else:
                if not stack: break
        return res