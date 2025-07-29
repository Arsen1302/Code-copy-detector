class Solution:
    def solution_1224_2(self, nums: List[int]) -> int:
        sum = nums[0]
        x = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                x += nums[i]
            else:
                x = nums[i]
            sum = max(x,sum)
            i += 1
        return sum