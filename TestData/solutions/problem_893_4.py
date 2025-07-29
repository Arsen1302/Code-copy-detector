class Solution:
    def solution_893_4(self, s: str, t: str) -> int:
        return sum((Counter(t)-Counter(s)).values())