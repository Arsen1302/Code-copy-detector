class Solution:
    def solution_123_4(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        
        tmp = 1
        for i in range(len(nums)-2,-1,-1):
            tmp *= nums[i+1]
            res[i] *= tmp
        
        return res