class Solution:
    def solution_1407_1(self, nums: List[int]) -> int:
        return next((i for i, x in enumerate(nums) if i%10 == x), -1)