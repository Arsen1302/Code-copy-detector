class Solution:
    def solution_486_4(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or set(s) != set(goal): return False
        goal += ''.join(goal)
        return s in goal