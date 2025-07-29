class Solution:
    def solution_1431_1(self, nums: List[int]) -> int:
        imin = nums.index(min(nums))
        imax = nums.index(max(nums))
        return min(max(imin, imax)+1, len(nums)-min(imin, imax), len(nums)+1+min(imin, imax)-max(imin, imax))