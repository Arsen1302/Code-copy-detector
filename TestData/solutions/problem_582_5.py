class Solution:
    def solution_582_5(self, nums: List[int]) -> bool:
        return sorted(nums) == nums or sorted(nums, reverse=True) == nums