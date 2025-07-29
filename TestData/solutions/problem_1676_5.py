class Solution:
    def solution_1676_5(self, nums: List[int]) -> int:
        return max([(n, len(list(g))) for n, g in itertools.groupby(nums)])[1]