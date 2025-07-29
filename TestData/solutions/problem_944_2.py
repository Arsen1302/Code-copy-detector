class Solution:
    def solution_944_2(self, nums: List[int]) -> int:
        #Take starting value as first elemet of the array
        startValue = 0
        
        #This will store the minimum step sum for all iterations
        minimum_num = 0
        
        #Iterate
        for i in nums:
            #StepSum
            startValue += i
            
            #Storing minimum possible step sum
            minimum_num = min(minimum_num, startValue)
        
        #Now if we add a number abs(minimum_num)+1, at each iteration stepsum will increase by this number and hence every stepsum is greater than 1    
        return 1-minimum_num