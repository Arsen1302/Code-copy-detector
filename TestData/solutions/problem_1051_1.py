class Solution:
    def solution_1051_1(self, nums: List[int]) -> int:
        return sum(bin(a).count('1') for a in nums) + len(bin(max(nums))) - 2 - 1