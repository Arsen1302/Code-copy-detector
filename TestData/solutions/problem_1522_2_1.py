class Solution:
    def solution_1522_2_1(self, nums: List[int]) -> int:

        def solution_1522_2_2(nums): #removing adjacent duplicates as they neither add to a hill or valley
            i = 1
            while i < len(nums):    
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    i -= 1  
                i += 1
            return nums
        nums=solution_1522_2_2(nums)

        count=0

        for i in range(1,len(nums)-1):
            
            if (nums[i-1]<=nums[i] and nums[i]>nums[i+1]) or (nums[i-1]>nums[i] and nums[i]<=nums[i+1]):
                count+=1
        return count