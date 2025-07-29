class Solution:
    def solution_271_5(self, nums: List[int]) -> int:
        
        distance = 0                  #hamming distance
        for i in range(30):
            
            mask = 1 << i             #mask will be power ith power of 2
            one , zero = 0 , 0
            for num in nums:
                
                if (num &amp; mask):      #a bit manupulation technique to check whether the ith bit is set 
                    one +=1
                else:
                    zero +=1
            distance += (one * zero)      
            
            
        return distance