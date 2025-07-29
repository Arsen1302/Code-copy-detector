class Solution:
    def solution_1711_1(self, nums: List[int], k: int) -> int:
        
        seen = collections.Counter(nums[:k]) #from collections import Counter (elements and their respective count are stored as a dictionary)
        summ = sum(nums[:k])
        
        
        res = 0
        if len(seen) == k:
            res = summ
            
            
        for i in range(k, len(nums)):
            summ += nums[i] - nums[i-k]
            seen[nums[i]] += 1
            seen[nums[i-k]] -= 1
            
            if seen[nums[i-k]] == 0:
                del seen[nums[i-k]]
                
            if len(seen) == k:
                res = max(res, summ) 
                
        return res