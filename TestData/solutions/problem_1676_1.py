class Solution:
    def solution_1676_1(self, nums: List[int]) -> int:
        max_n = max(nums)
        return max(len(list(it)) for n, it in groupby(nums) if n == max_n)