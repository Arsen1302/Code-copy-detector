class Solution:
    def solution_102_3(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]