class Solution:
    def solution_252_1(self, nums: List[int]) -> int:
        return sum(nums) - (len(nums) * min(nums))