class Solution:
    def solution_1224_1(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums): 
            if not i or nums[i-1] >= nums[i]: val = 0 # reset val 
            val += nums[i]
            ans = max(ans, val)
        return ans