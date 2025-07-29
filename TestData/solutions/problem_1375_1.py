class Solution:
    def solution_1375_1(self, nums: List[int]) -> int:
        beauty=[0]*len(nums)
        for i in range(1,len(nums)-1):
            leftarr=nums[:i]
            rightarr=nums[i+1:]
            if(max(leftarr)<nums[i] and min(rightarr)>nums[i]):
                beauty[i]=2
            elif(nums[i-1]<nums[i] and nums[i+1]>nums[i]):
                beauty[i]=1
            else:
                beauty[i]=0
        return sum(beauty)