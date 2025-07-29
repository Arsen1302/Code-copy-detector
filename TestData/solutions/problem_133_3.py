class Solution:
    def solution_133_3(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)