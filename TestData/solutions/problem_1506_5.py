class Solution:
    def solution_1506_5(self, nums, key):
        return mode(b for a, b in pairwise(nums) if a == key)