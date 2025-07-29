class Solution:
    def solution_223_4(self, nums: List[int]) -> int:
        return max(nums) if len(set(nums)) < 3 else sorted(list(set(nums)))[-3]