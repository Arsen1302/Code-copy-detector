class Solution:
    def solution_1476_5(self, nums: List[int]) -> int:
        return len([num for num in nums if num not in {min(nums),max(nums)}])