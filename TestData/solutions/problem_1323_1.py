class Solution:
    def solution_1323_1(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1