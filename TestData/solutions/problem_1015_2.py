class Solution:
    def solution_1015_2(self, nums: List[int]) -> int:
        return min(x-y for x, y in zip(nlargest(4, nums), reversed(nsmallest(4, nums))))