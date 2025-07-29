class Solution:
    def solution_1627_5(self, nums: List[int]) -> int:
        count = 0
        while max(nums) != 0:
            minValue = float('inf')
            for i in range(len(nums)):
                if nums[i] != 0 and nums[i] < minValue:
                    minValue = nums[i]
            for i in range(len(nums)):
                nums[i] = max(nums[i] - minValue, 0)
            count += 1
        return count