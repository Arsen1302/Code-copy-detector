class Solution:
    def solution_104_1(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)