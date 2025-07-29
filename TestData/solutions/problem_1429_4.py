class Solution:
    def solution_1429_4(self, nums, target):
        idx = sum(num < target  for num in nums)
        cnt = sum(num == target for num in nums)
        return list(range(idx, idx+cnt))