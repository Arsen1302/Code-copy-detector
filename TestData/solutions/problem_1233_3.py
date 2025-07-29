class Solution:
    def solution_1233_3(self, nums: List[int]) -> int:
        rev_nums = [int(str(num)[::-1]) for num in nums]
        c = collections.Counter([i-j for i, j in zip(nums, rev_nums)])
        return sum([freq * (freq-1) // 2 for _, freq in c.items() if freq > 1]) % int(1e9+7)