class Solution:
    def solution_1242_3(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return 0
        
        ans=0
        
        for i in range(1,n):
            if(nums[i]<=nums[i-1]):
                ans+=nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
        
        return ans