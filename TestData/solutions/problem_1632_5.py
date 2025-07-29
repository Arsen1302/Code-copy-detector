class Solution:
    def solution_1632_5(self, nums: List[int]) -> int:
        n=len(nums)
        countgood=0
        d=dict()
        for i in range(len(nums)):
            diff=i-nums[i]
            if diff not in d:
                d[diff]=1
            else:
                d[diff]+=1
        for key,value in d.items():
            countgood+=(value*(value-1)//2)
        totalpairs=n*(n-1)//2        
        return totalpairs-countgood