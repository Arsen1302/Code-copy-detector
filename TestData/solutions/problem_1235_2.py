class Solution:
    def solution_1235_2(self, s: str, k: int) -> str:
        l = list(s.split(" "))
        return (" ".join(l[:k]))