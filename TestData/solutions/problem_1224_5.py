class Solution:
    def solution_1224_5(self, nums: List[int]) -> int:
        maxSum = 0
        subSum = 0
        
        for i in range(len(nums)):
            
            if i == 0 or nums[i-1] < nums[i]:
                subSum += nums[i]
                maxSum = max(maxSum, subSum)
            else:
                subSum = nums[i]
                
        return maxSum