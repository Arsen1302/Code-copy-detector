class Solution:
    def solution_1566_5(self, nums: List[int]) -> int:
        
        array = list(accumulate(nums, operator.add))
        count=0
        end = array[-1]
        for i in range (len(array)-1):
            
            left = array[i]-0
            right = end - array[i]
            
            if left >= right: count+=1
                
        return count