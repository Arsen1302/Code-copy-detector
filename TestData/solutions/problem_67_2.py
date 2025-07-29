class Solution:
    def solution_67_2(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi: 
            mid = lo + hi >> 1
            if nums[mid] < nums[hi]: hi = mid
            elif nums[mid] == nums[hi]: hi -= 1 # duplicates
            else: lo = mid + 1
        return nums[lo]