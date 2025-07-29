class Solution:
    def solution_258_4(self, s: str) -> bool:
        return s in s[1:]+s[:-1]