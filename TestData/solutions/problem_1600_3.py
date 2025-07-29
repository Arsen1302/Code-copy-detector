class Solution:
    def solution_1600_3(self, nums: List[int]) -> int:
        return reduce(operator.or_, nums)