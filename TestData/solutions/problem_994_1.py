class Solution(object):
    def solution_994_1(self, nums):
        result = []
        current_sum = 0
        for i in range(0, len(nums)):
            result.append(current_sum + nums[i])
            current_sum = result[i]
        return result