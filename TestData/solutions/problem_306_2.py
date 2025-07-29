class Solution:
    def solution_306_2(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))