class Solution:
    def solution_1360_5(self, nums: List[int]) -> int:
        
        # find the sum
        right_sum = sum(nums)
        left_sum = 0
        
        for idx in range(len(nums)):
            
            # subtract current num from right sum
            right_sum -= nums[idx]
            
            # compare the sums
            if right_sum == left_sum:
                return idx
            
            # add current value to left sum
            left_sum += nums[idx]
        return -1