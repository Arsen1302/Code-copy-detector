class Solution:
    def solution_1235_4(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])