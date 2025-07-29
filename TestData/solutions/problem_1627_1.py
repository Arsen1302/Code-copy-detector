class Solution:
    def solution_1627_1(self, nums: List[int]) -> int:
        return len(set(nums) - {0})