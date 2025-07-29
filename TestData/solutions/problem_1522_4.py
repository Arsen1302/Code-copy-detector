class Solution:
    def solution_1522_4(self, nums: List[int]) -> int:
        n=0
        i=0
        l=len(nums)
        new=0 # to keep track of whether nums[i] is part of nums[0]
        prev=-1
        while i <l-1:
            if i ==0:
                pass
            elif nums[i-1]<nums[i]>nums[i+1]:
                n+=1
            elif nums[i-1]>nums[i]<nums[i+1]:
                n+=1
            elif new==1 and (prev<nums[i-1]==nums[i]>nums[i+1]):
                n+=1
            elif new==1 and (prev>nums[i-1]==nums[i]<nums[i+1]):
                n+=1
            if nums[i]!=nums[0]: #change new flag when the first time nums[i] is different from nums[0]
                new=1
            if nums[i]!=nums[i+1]:
                prev = nums[i]   #track previous different number
            i+=1
        return n