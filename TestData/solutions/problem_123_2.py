class Solution:
    def solution_123_2(self, nums: List[int]) -> List[int]:
        res = []
        
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * p #1
            p = p*nums[i]
        
        return res