class Solution:
    def solution_1566_4(self, nums: List[int]) -> int:
        n = len(nums)
        left_window_sum = nums[0]
        right_window_sum = sum(nums[1:])
        
        count = 0
        split_pos = 0

        while split_pos <= n-2:
            if left_window_sum >= right_window_sum:
                count += 1
            
            split_pos += 1
            left_window_sum += nums[split_pos]
            right_window_sum -= nums[split_pos]
            
        return count