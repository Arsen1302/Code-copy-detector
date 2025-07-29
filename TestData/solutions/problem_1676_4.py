class Solution:
    def solution_1676_4(self, nums: List[int]) -> int:
        x = max(nums)
        res = 1
        for c, g in itertools.groupby(nums): 
            if c == x: 
                res = max(res, len(list(g)))
        return res