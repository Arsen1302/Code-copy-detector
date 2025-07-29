class Solution:
    def solution_325_4(self, s: str) -> bool:
        return s.count("A") < 2 and "LLL" not in s