class Solution:
    def solution_1316_1(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums