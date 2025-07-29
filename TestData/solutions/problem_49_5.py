class Solution:
    def solution_49_5(self, nums: List[int]) -> int:
        return sum(list(set(nums)) * 2) - sum(nums)