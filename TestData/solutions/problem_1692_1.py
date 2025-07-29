class Solution:
    def solution_1692_1(self, nums: List[int]) -> int:
        return max(ceil(n / (i + 1)) for i, n in enumerate(accumulate(nums)))