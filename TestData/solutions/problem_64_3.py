class Solution:
    def solution_64_3(self, s: str) -> str:
        return ' '.join([ch for ch in reversed(s.split()) if ch])