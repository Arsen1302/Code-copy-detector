class Solution:
    def solution_1542_4(self, nums: List[int]) -> int:
       
        closest = 0
        if 0 in nums:
            return 0
      
        for i in range(len(nums)):
                       
            if closest == 0 : 
                closest = nums[i]
            elif nums[i] > 0 and nums[i] <= abs(closest):
                closest = nums[i]
            elif nums[i] < 0 and nums[i] < abs(closest) and abs(nums[i]) < abs(closest):
                closest = nums[i]

        return closest
    
    
   
    ```