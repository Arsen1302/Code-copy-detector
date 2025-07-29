class Solution:
    def solution_1694_3(self, nums: List[int]) -> int:
        return max(list(filter(lambda x: nums.count(x) >= 1 and nums.count(-x) >= 1, nums)) + [-1])