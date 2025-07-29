class Solution:
    def solution_1526_4(self, nums: List[int]) -> int:
        
        res = 0
        i = 0
        n = len(nums)
        
        while i < n-1:
            if nums[i] == nums[i+1]:
                res += 1
                i += 1
            else:
                i += 2
            
        if nums[n-1] == nums[n-2]:
            res += 1
        
        if (n - res) % 2:
            res += 1
            
        return res