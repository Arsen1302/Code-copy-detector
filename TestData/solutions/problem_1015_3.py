class Solution:
    def solution_1015_3(self, nums: List[int]) -> int:
        small = nsmallest(4, nums)
        large = nlargest(4, nums)
        return min(x-y for x, y in zip(large, reversed(small)))