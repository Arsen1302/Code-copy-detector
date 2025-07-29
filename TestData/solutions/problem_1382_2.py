class Solution:
    def solution_1382_2(self, nums, target):
        return sum(i + j == target for i, j in permutations(nums, 2))