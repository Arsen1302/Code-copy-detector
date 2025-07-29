class Solution:
    def solution_1429_2(self, nums, target):
        return [i for i,num in enumerate(sorted(nums)) if num==target]