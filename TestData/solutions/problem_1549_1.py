class Solution:
    def solution_1549_1(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &amp;= set(nums[i])
        res = list(res)
        res.sort()
        return res