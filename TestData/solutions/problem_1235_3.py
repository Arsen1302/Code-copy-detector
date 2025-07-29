class Solution:
    def solution_1235_3(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])