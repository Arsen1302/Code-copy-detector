class Solution:
    def solution_278_4(self, nums: List[int]) -> int:
        
        ans = 0
        j = 0
        
        for i in range(len(nums)):
            
            if nums[i] == 1:
                j += 1
                
            else:
                j = 0
                
            ans = max(ans, j)
            
        return ans