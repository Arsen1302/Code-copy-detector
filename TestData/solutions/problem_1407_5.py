class Solution:
    def solution_1407_5(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i % 10 == nums[i]:
                return i
        
        return -1