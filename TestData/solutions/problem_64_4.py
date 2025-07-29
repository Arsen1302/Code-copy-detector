class Solution:
    def solution_64_4(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        return " ".join(s[::-1])