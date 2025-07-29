class Solution:
    def solution_447_5(self, nums):
        max1_val, max1_idx, max2_val = -1, -1, -1
        
        for i,n in enumerate(nums):
            if n > max1_val:
                max2_val = max1_val
                max1_val, max1_idx = n, i
            elif n > max2_val:
                max2_val = n
        
        return max1_idx if max1_val >= max2_val*2 else -1