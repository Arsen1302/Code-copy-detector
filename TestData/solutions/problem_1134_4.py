class Solution:
     def solution_1134_4(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0;j=len(nums)-1
        ans=0
        while i<j:
            Sum=nums[i]+nums[j]
            if Sum==k:
                i+=1
                j-=1
                ans+=1
            elif Sum<k:
                i+=1
            else:
                j-=1
        return ans