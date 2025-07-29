class Solution:
    def solution_1676_2(self, nums: List[int]) -> int:
        maxim = max(nums)
        result = 1
        current = 0
        for num in nums:
            if (num == maxim):
                current = current + 1
                result = max(result, current)
            else:
                current = 0
        return result