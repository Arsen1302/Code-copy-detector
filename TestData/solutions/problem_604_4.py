class Solution:
    def solution_604_4(self, nums: List[int]) -> List[int]:
        
        l,r=0,len(nums)-1
        
        while l<len(nums) and r>0:
            
            if nums[l]%2==0: l+=2
                
            elif nums[r]%2!=0: r-=2
            
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=2
                r-=2
               
        return nums