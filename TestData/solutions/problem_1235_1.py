class Solution:
    def solution_1235_1(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(words[0:k])