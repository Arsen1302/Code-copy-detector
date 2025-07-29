class Solution:
    def solution_1309_5(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]