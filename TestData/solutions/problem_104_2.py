class Solution:
    def solution_104_2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)