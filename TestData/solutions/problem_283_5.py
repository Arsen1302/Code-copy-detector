class Solution:
    def solution_283_5(self, nums: List[int]) -> int:
        t = []
        res = 0
        for i in range(len(nums)):
            j = bisect.bisect_right(t, 2*nums[i])
            res += len(t) - j
            bisect.insort(t, nums[i])
        return res