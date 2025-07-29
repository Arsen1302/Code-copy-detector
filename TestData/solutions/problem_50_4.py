class Solution:
    def solution_50_4(self, nums: List[int]) -> int:
        a, b = 0, 0
        for c in nums:
            b = (b ^ c) &amp; ~a
            a = (a ^ c) &amp; ~b
        return b