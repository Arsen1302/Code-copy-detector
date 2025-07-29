class Solution:
    def solution_337_2(self, nums: List[int]) -> int:
        ans = cnt = 0
        for i, idx in enumerate(nums):
            if idx < 0: continue                           # avoid revisit
            while nums[idx] >= 0:
                cnt, nums[idx], idx = cnt+1, -1, nums[idx] # increment length; mark as visited; visit next value
            else:    
                ans, cnt = max(ans, cnt), 0                # record length and reset `cnt`
        return ans