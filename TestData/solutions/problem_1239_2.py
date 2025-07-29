class Solution:
    def solution_1239_2(self, nums: List[int]) -> int:
        signs = False
        for x in nums:
            if x == 0 : return 0
            signs = signs ^ (x < 0)
        if signs : return -1
        else: return 1