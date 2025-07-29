class Solution:
    def solution_260_5(self, nums: List[int]) -> int:
        m = sorted(nums)[len(nums)//2] # median
        return sum(abs(x-m) for x in nums)