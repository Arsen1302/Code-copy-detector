class Solution:
    def solution_769_5(self, nums: List[int]) -> int:
        ans = [0, 0] 
        for i in range(len(nums)): 
            val = 0 
            if i: val = max(val, nums[i] - nums[i-1] + 1)
            if i+1 < len(nums): val = max(val, nums[i] - nums[i+1] + 1)
            ans[i&amp;1] += val
        return min(ans)