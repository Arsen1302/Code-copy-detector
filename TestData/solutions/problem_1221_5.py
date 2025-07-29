class Solution:
    def solution_1221_5(self, s: str) -> int:
        return ([-1, -1] + sorted(set(int(c) for c in s if c.isdigit())))[-2]