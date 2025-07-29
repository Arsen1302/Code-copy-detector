class Solution:
    def solution_319_5(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
        # return reduce(xor, nums)  # one-liner