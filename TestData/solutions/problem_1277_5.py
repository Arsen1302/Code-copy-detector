class Solution:
    def solution_1277_5(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0 
        l, r = 0, n-1
        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        return res