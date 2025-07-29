class Solution:
    def solution_1186_2(self, nums: List[int]) -> int:
        min_sum = nums[0]
        curr_min = nums[0]
        
        max_sum = nums[0]
        curr_max = max_sum
        
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(curr_max, max_sum)
        
        for i in range(1, len(nums)):
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(curr_min, min_sum)
        
        return max(abs(max_sum), abs(min_sum))