class Solution:
    def solution_1530_5(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        newNums = []
        for i in range(len(nums)-1):
            k = (nums[i] + nums[i+1]) % 10
            newNums.append(k)
            
        return self.solution_1530_5(newNums)