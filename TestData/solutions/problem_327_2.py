class Solution:
    def solution_327_2(self, nums: List[int]) -> str:
        return "/".join(map(str, nums)) if len(nums) <= 2 else f'{nums[0]}/({"/".join(map(str, nums[1:]))})'