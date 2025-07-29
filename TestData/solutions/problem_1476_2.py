class Solution:
    def solution_1476_2(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        c=0
        for i in range(len(nums)):
            if nums[i]>mi and nums[i]<ma:
                c+=1
        return c