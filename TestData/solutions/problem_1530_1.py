class Solution:
    def solution_1530_1(self, nums: List[int]) -> int:
        return sum(n * comb(len(nums) - 1, i) for i, n in enumerate(nums)) % 10