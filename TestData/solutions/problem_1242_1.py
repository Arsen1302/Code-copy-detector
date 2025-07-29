class Solution:
    def solution_1242_1(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                x = nums[i]
                nums[i] += (nums[i-1] - nums[i]) + 1
                count += nums[i] - x
        return count