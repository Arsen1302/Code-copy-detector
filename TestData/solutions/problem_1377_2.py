class Solution:
    def solution_1377_2(self, nums: List[int]) -> int:
        mn,mx=float('inf'),-1
        for i in range(len(nums)):
            mn=min(mn,nums[i])
            mx=max(mx,nums[i]-mn)
        if mx==0: return -1
        return mx