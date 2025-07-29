class Solution(object):
    def solution_248_5(self, nums):
        return set(range(1,len(nums)+1)) - set(nums)