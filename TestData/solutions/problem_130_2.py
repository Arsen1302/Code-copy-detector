class Solution:
    def solution_130_2(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        return([y for y in x if x[y] == 1])