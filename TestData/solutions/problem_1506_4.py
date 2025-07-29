class Solution:
    def solution_1506_4(self, nums, key):
        return mode(nums[i] for i in range(1,len(nums)) if nums[i-1]==key)