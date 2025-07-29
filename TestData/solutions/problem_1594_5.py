class Solution:
    def solution_1594_5(self, s: str) -> str:
        return max(Counter(s) &amp; Counter(s.swapcase()), default="").upper()