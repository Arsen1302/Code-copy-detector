class Solution:
    def solution_1663_1(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        return max([c for c in ctr if not c%2], key = lambda x:(ctr[x], -x), default = -1)