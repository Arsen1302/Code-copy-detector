class Solution:
    def solution_486_1(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal