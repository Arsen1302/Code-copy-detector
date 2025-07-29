class Solution:
    def solution_1503_1(self, s: str, t: str) -> int:
        fs, ft = Counter(s), Counter(t)
        return sum((fs-ft).values()) + sum((ft-fs).values())