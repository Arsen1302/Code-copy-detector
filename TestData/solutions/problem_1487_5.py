class Solution:
    def solution_1487_5(self, nums: List[int]) -> List[int]:
        nums[0::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2])[::-1]
        return nums