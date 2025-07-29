class Solution:
    def solution_1309_4(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        
        for n in nums:
            result[n] = nums[nums[n]]
            
        return result