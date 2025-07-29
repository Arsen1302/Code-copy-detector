class Solution:
    def solution_1370_3(self, nums: List[int], k: int) -> int:
        count = 0
        
        hash = {}
        
        for i in nums:
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1
                
        for i in hash:
            if i+k in hash:
                count+=hash[i]*hash[i+k]
                
        return count