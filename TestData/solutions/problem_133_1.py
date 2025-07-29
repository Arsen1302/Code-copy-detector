class Solution:
    def solution_133_1(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)