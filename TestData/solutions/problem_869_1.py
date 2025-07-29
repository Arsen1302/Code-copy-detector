class Solution:
    def solution_869_1(self, a: int, b: int, c: int) -> int:   
        count = 0
        while a or b or c:
            if (a &amp; 1) | (b &amp; 1) != (c &amp; 1):
                if (c &amp; 1): count += 1
                else: count += (a &amp; 1) + (b &amp; 1)
            a, b, c = a >> 1, b >> 1, c >> 1
        return count