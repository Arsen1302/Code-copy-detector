class Solution(object):
    def solution_1622_4(self, nums):
        ans, count = 0, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                ans += count
                count += 1
            else: count = 1
        return ans