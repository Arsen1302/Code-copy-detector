class Solution:
    def solution_65_2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        min_so_far, max_so_far, max_global = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_so_far, min_so_far = max(min_so_far*nums[i], max_so_far*nums[i], nums[i]), min(min_so_far*nums[i], max_so_far*nums[i], nums[i])
            max_global = max(max_global, max_so_far)
        
        return max_global