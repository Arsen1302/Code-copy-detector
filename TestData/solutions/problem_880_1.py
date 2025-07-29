class Solution:
    def solution_880_1(self, s: str) -> int:
        return 1 if s == s[::-1] else 2