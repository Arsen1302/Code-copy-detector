class Solution:
    def solution_243_5(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = (nums[i]%len(nums))-1 #As value from 1-n
            nums[index]+=len(nums)
        output = []
        for i,v in enumerate(nums):
            if v>2*len(nums):
                output.append(i+1)
        return output