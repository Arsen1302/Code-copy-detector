class Solution:
    def solution_1429_1(self, nums, target):
        ans = []
        for i,num in enumerate(sorted(nums)):
            if num == target: ans.append(i)
        return ans