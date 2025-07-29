class Solution:
    def solution_1651_1(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, q) for q in queries]