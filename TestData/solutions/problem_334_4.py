class Solution:
    def solution_334_4(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        for i in range(0, len(nums), 2):
            summ += nums[i]
        return summ