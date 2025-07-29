class Solution:
    def solution_252_4(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)