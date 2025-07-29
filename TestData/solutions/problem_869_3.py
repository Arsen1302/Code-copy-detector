class Solution:
    def solution_869_3(self, a, b, c):
        count = lambda x : bin(x).count('1')
        return count((a | b) ^ c) + count(a &amp; b &amp; ~c)