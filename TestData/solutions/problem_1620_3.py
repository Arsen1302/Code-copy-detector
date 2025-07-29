class Solution:
    def solution_1620_3(self, nums: List[int], numsDivide: List[int]) -> int:
        g = reduce(gcd, numsDivide)
        return next((i for i, x in enumerate(sorted(nums)) if g % x == 0), -1)