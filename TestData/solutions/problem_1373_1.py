class Solution:
    def solution_1373_1(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        
        ans = ii = 0
        for i, x in enumerate(nums): 
            if x - nums[ii] >= n: ii += 1
            ans = max(ans, i - ii + 1)
        return n - ans