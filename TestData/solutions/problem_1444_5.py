class Solution:
    def solution_1444_5(self, words: List[str]) -> str:
        return next(s for s in words + [''] if s == s[::-1])