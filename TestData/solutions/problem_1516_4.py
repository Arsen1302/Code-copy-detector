class Solution:
    def solution_1516_4(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k&amp;1: return -1
        ans = 0 
        for i in range(min(k-1, len(nums))): ans = max(ans, nums[i])
        if k < len(nums): ans = max(ans, nums[k])
        return ans