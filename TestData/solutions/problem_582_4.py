class Solution:
    def solution_582_4(self, nums):
        return all(a >= b for a,b in pairwise(nums)) or all(b >= a for a,b in pairwise(nums))