class Solution(object):
    def solution_50_1(self, nums):
        a, b = 0, 0
        for x in nums:
            a, b = (~x&amp;a&amp;~b)|(x&amp;~a&amp;b), ~a&amp;(x^b)
        return b