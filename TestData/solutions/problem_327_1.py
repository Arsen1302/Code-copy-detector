class Solution:
    def solution_327_1(self, nums: List[int]) -> str:
        if len(nums) <= 2: return "/".join(map(str, nums))
        return f'{nums[0]}/({"/".join(map(str, nums[1:]))})'