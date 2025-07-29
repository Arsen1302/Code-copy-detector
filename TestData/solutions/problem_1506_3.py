class Solution:
    def solution_1506_3(self, nums, key):
        return max(c := Counter([nums[i] for i in range(1,len(nums)) if nums[i-1]==key]), key=c.get)