class Solution:
    def solution_71_2(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        nums.sort()
        max_diff=0
        for i in range(len(nums)-1):
            max_diff=max(max_diff,nums[i+1]-nums[i])
        return max_diff