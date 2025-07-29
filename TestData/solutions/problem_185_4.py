class Solution:
    def solution_185_4(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b &amp; mask: 
            a, b = a^b, (a&amp;b) << 1
        return a &amp; mask if b > mask else a