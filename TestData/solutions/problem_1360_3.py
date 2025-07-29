class Solution:
    def solution_1360_3(self, nums: List[int]) -> int:
        total = sum(nums)
        size = len(nums)
        for i in range(size):
            if (sum(nums[:i]) == sum(nums[i+1:])) and i < (size - 1) :
                return i
            elif i == (size - 1) and (total-nums[-1]) == 0:
                return (size - 1)
        return -1