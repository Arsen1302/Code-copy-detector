class Solution:
    def solution_1195_4_1(self, nums, maxSize, maxOp):
        requiredOp=0
        for num in nums:
            op=(num-1)//maxSize
            requiredOp+=op
        return requiredOp<=maxOp

    def solution_1195_4_2(self, nums, maxOp):
        lo=1 ; hi=max(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if self.solution_1195_4_1(nums,mid,maxOp): hi=mid
            else: lo=mid+1
        return hi