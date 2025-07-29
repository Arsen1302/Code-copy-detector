class Solution:
    def solution_133_2(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, list(range(len(nums)+1)) + nums)