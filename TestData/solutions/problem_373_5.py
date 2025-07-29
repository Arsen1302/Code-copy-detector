class Solution(object):
    def solution_373_5(self, nums):
        l, dup, mis = len(nums), 0, 0
        for num in nums:
            if nums[abs(num) - 1] < 0 :
                dup = abs(num)
            else: nums[abs(num) - 1] *= -1
        
        for index in range(l):
            if nums[index] > 0:
                mis = index + 1
                break
                
        return [dup, mis]