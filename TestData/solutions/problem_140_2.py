class Solution(object):
    def solution_140_2(self, nums):
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c],nums[i]=nums[i],nums[c]
                c+=1
        return nums