class Solution:
    def solution_1549_2(self, nums: List[List[int]]) -> List[int]:
        res = []
        concat = []
        for i in range(len(nums)):
            concat += nums[i]
        for i in set(concat):
            if concat.count(i) == len(nums):
                res.append(i)
        return sorted(res)