class Solution:
    def solution_1520_2(self, nums: List[int]) -> int:
        s = sum(nums)
        
        nums = [-i for i in nums]
        heapify(nums)
        
        total, halve, res = s, s/2, 0
        while total > halve:
            total += nums[0]/2
            heapreplace(nums, nums[0]/2)
            res += 1
            
        return res