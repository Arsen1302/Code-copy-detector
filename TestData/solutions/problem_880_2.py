class Solution:
    def solution_880_2(self, s: str) -> int:
        return int(s==s[::-1]) or 2