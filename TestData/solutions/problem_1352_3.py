class Solution:
    def solution_1352_3(self, nums: List[int]) -> int:
        minV, maxV = min(nums), max(nums)
        return max ([k for k in range(1, min (minV, maxV)+1) if minV % k == 0 and maxV % k == 0])