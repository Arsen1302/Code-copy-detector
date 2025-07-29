class Solution:
    def solution_334_2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        
# Time : 332 ms
# Memory : 16.5 M