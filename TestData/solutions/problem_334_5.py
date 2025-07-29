class Solution:
    def solution_334_5(self, nums: List[int]) -> int:
        nums = sorted(nums) 
        return sum([nums[i] for i in range(0, len(nums), 2)])