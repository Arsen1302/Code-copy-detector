class Solution:
    def solution_1554_5(self, nums: List[int]) -> int:
        S, n = sum(nums), len(nums)
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        
        min_diff, min_index = float('inf'), -float('inf')
        for i in range(len(nums)):
            if n - i - 1 != 0:
                abs_diff = abs(prefixSum[i] // (i+1) - (S - prefixSum[i]) // (n - i - 1))
            else:
                abs_diff = abs(prefixSum[i] // (i+1))
            if abs_diff < min_diff:
                min_diff = abs_diff
                min_index = i
                
        return min_index