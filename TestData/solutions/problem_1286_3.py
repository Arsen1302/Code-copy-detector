class Solution:
    def solution_1286_3(self, nums: List[int]) -> int:
        nums, n = sorted(nums), len(nums)
        return sum([n-i if nums[i-1] != nums[i] else 0 for i in range(1, n)])