class Solution:
    def solution_1213_2(self, s: str) -> bool:
        s = s.strip("0")
        return ("0" not in s)