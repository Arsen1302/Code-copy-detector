class Solution:
    def solution_848_2(self, nums: List[int]) -> int:
        
        counter = 0
        
        for number in nums:
            
            if len( str(number) ) % 2 == 0:
                
                counter += 1
                
        return counter