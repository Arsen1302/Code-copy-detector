class Solution:
    def solution_1360_2(self, nums: List[int]) -> int:
        A = [0] + list(accumulate(nums)) + [0]
        total, n = sum(nums), len(nums)
        for i in range(n):
            if A[i] == total - A[i] - nums[i]:
                return i
        return -1