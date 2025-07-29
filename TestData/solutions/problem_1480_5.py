class Solution(object):
    def solution_1480_5(self, nums, original):
        
        s = set(nums)
        
        while original in s:
            original *=2
            
        return original