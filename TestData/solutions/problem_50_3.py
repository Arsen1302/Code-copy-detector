class Solution(object):
    def solution_50_3(self, nums):
        a = sum(nums) - 3*sum(set(list(nums)))
        return (-a)//2