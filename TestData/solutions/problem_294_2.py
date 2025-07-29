class Solution:
    def solution_294_2(self, nums: List[int]) -> List[str]:
        if len(nums)==1:
            return ["Gold Medal"]
        elif len(nums)==2:
            if nums[0]>nums[1]:
                nums[0],nums[1]="Gold Medal","Silver Medal"
            else:
                nums[1],nums[0]="Gold Medal","Silver Medal"
            return nums
        l=sorted(nums)
        fmax,smax,tmax=l[-1],l[-2],l[-3]
        d={}
        for i,j in enumerate(l):
            d[j]=i
        for i in range(len(nums)):
            if nums[i]==fmax:
                nums[i]="Gold Medal"
            elif nums[i]==smax:
                nums[i]="Silver Medal"
            elif nums[i]==tmax:
                nums[i]="Bronze Medal"
            else:
                nums[i]=str(len(nums)-d[nums[i]])
        return nums