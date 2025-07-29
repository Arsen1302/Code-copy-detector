class Solution:
    def solution_334_3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])