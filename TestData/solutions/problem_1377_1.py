class Solution:
    def solution_1377_1(self, nums: List[int]) -> int:
        ans = -1 
        prefix = inf
        for i, x in enumerate(nums): 
            if i and x > prefix: ans = max(ans, x - prefix)
            prefix = min(prefix, x)
        return ans