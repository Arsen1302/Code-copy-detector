class Solution:
    def solution_1637_2(self, nums: List[int]) -> bool:
        f3,f2,f1 = False,False,True
        for i,v in enumerate(nums):
            f = f2 and (v==nums[i-1])
            f = f or f3 and (v==nums[i-1]==nums[i-2])
            f = f or f3 and (v==nums[i-1]+1==nums[i-2]+2)
            f3,f2,f1 = f2,f1,f
        return f1