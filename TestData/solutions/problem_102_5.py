class Solution:
    def solution_102_5(self, nums, k):
        pivot = nums[0]
        
        left = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if k <= len(right): return self.solution_102_5(right, k)
        elif len(right) < k <= len(right) + len(equal): return equal[0]
        else: return self.solution_102_5(left, k - len(right) - len(equal))

# Average Time Complexity: O(N)
# Worst Case Time Complexity: O(N^2)
# Space Complexity: O(N)