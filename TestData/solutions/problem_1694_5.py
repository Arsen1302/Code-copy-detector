class Solution:
    def solution_1694_5(self, nums: List[int]) -> int:
        res = -1
        s = set()
        for num in nums:
            if -num in s:
                res = max(res, abs(num))
            s.add(num)
        return res