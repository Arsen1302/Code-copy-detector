class Solution:
    def solution_397_5(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        longest = 0
        starting, ending = 0, 0 
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                ending += 1
            else:
                ending += 1
                longest = max(longest, (ending-starting))
                starting = ending

        ending += 1
        longest = max(longest, (ending-starting))

        return longest