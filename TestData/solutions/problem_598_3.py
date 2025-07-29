class Solution:
    def solution_598_3(self, nums: List[int]) -> int:
        ans=0
        maxo=nums[0]
        maxtn=nums[0]
        for i in range(len(nums)):
            if nums[i]>=maxtn:
                pass
            else:
                ans=i
                maxtn=max(maxtn,nums[i],maxo)
            maxo=max(nums[i],maxo)
        return ans+1