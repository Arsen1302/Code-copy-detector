class Solution:
    def solution_1360_4(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i, x in enumerate(nums): 
            if 2*prefix == total - x: return i
            prefix += x
        return -1