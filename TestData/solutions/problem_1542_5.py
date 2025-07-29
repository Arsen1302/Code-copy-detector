class Solution:
    def solution_1542_5(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if abs(nums[i]) in d:
                d[abs(nums[i])]=max(d[abs(nums[i])],nums[i])
            else:
                d[abs(nums[i])]=nums[i]
        return d[min(d.keys())]