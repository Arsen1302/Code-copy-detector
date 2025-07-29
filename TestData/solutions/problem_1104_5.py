class Solution:
    def solution_1104_5(self, nums):
        c = Counter(nums)
        nums.sort(key=lambda x: (c[x], -x))
        return nums