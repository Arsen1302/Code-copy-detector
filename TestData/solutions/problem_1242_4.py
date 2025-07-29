class Solution:
    def solution_1242_4(self, nums: List[int]) -> int:
        s = 0
        for i in range(1,len(nums)):
            s += max(0,nums[i-1]-nums[i]+1)
            nums[i] = max(nums[i-1]+1, nums[i])
        return s