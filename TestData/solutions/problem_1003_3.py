class Solution:
    def solution_1003_3(self, nums: List[int]) -> int:
        start, max_window, ones_count = 0,0,0
        
        for end in range(len(nums)):
            ones_count += nums[end]
            
            if (end - start + 1 - ones_count) > 1:
                ones_count -= nums[start]
                start += 1
                
            max_window = max(max_window, end - start + 1)
        return max_window - 1