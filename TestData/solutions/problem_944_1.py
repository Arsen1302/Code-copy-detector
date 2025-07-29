class Solution:
    def solution_944_1(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)): nums[i] = nums[i] + nums[i - 1]
        
        return 1 if min(nums) >= 1 else abs(min(nums)) + 1