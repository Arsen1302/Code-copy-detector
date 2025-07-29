class Solution:
    def solution_1584_2(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=1
        minm=nums[0]
        maxm=nums[0]
        for x in nums:
            if abs(x-minm)>k or abs(x-maxm)>k:
                res+=1
                minm=x
                maxm=x
            else:
                minm=min(minm,x)
                maxm=max(maxm,x)
        return res