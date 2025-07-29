class Solution:
    def solution_223_2(self, nums: List[int]) -> int:
        
        max1 = nums[0]  #Initialised the max with first index
        secmax = float('-inf') 
        thirmax = float('-inf')
        #assuming second and third to be -infinity
        
        if len(nums)<3:
                return max(nums)
        #this won't run more than 2 times and hence we can consider this in our O(n) solution!
        # It isn't worth writing the Whole Loop logic here
        
        for i in range(len(nums)):
                num = nums[i]
                
				#Read the below if conditions to get the approach of updating First, second and third max respectively
				
                if (num>max1):
                        thirmax = secmax 
                        secmax = max1
                        max1 = nums[i]
                        
                elif(num>secmax and num<max1):
                        thirmax = secmax
                        secmax = num
                        
                elif(num>thirmax and num<secmax):
                        thirmax = num
                        
        return thirmax if thirmax != float('-inf') else max1
		#if condition when the elements get repeated such that thirdmax remains -infinity