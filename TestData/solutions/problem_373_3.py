class Solution:
    def solution_373_3(self, nums: List[int]) -> List[int]:
        toRemove = sum(nums) - sum(set(nums))
        actualMissing = sum(range(1, len(nums)+1)) - sum(set(nums))
        return [toRemove, actualMissing]