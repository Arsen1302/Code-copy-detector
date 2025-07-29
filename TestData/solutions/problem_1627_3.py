class Solution:
    def solution_1627_3(self, nums: List[int]) -> int:
        nums = set(nums)
        if 0 in nums:
            return(len(nums)-1)
        else:
            return(len(nums))