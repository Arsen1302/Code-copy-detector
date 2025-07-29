class Solution:
    def solution_1286_4(self, nums: List[int]) -> int:
        nums= sorted(nums)
        res, val = 0, 0 
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] : 
                res +=1 
            val += res 
        return val