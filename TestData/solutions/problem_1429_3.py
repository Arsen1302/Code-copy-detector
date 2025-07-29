class Solution:
    def solution_1429_3(self, nums, target):
        idx = cnt = 0
        for num in nums:
            idx += num < target
            cnt += num == target
        return list(range(idx, idx+cnt))