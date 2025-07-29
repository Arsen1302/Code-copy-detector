class Solution:
    def solution_1224_3(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for i in range(len(nums) + 1):
            if i != 0:
                if result < count:
                    result = count
                if i != len(nums):
                    if nums[i - 1] >= nums[i]:
                        count = 0
            if i != len(nums):
                count += nums[i]

        return result