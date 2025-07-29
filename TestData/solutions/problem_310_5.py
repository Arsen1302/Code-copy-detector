class Solution:
    def solution_310_5(self, nums: List[int]) -> int:
        seen = {0: -1}
        ans = prefix = 0
        for i, x in enumerate(nums):
            prefix += 2*x-1
            ans = max(ans, i - seen.setdefault(prefix, i))
        return ans