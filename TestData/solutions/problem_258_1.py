class Solution:
    def solution_258_1(self, s: str) -> bool:
        return s in s[1:] + s[:-1]