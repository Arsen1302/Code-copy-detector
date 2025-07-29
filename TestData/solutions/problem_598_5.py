class Solution:
    def solution_598_5(self, nums: List[int]) -> int:
        n = len(nums)
        left_length = 1 
        left_max = curr_max = nums[0] 
        for i in range(1, n-1): 
            if nums[i] < left_max:
                left_length = i+1
                left_max = curr_max
            else:
                curr_max = max(curr_max, nums[i])
        return left_length