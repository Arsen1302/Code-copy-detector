class Solution:
    def solution_114_5(self, nums: List[int]) -> List[str]:
        ans=[] ; i=0 ; nums.append(-1)
        for j in range(len(nums)-1):
            if nums[j+1]!=1+nums[j]: 
                if i!=j: ans.append(str(nums[i])+'->'+str(nums[j])) ; i=j+1
                else   : ans.append(str(nums[i])) ; i=j+1
        return ans