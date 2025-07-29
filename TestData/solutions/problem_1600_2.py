class Solution:
    def solution_1600_2(self, nums: List[int]) -> int:
        return reduce(or_, nums)