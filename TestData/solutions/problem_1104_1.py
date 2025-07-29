class Solution:
    def solution_1104_1(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums,reverse=1),key=nums.count)