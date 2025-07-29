class Solution:
    def solution_893_3(self, s: str, t: str) -> int:
        common_vals = sum((Counter(s) &amp; Counter(t)).values())
        return len(s) - common_vals