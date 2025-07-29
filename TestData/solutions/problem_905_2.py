class Solution:
    def solution_905_2(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        res = []
        for i in nums:
            res.append(sort_nums.index(i))
        return res