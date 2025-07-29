class Solution(object):
    def solution_1407_2(self, nums, i=0):
        return -1 if i == len(nums) else ( i if i%10 == nums[i] else self.solution_1407_2(nums, i+1) )