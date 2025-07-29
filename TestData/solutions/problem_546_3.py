class Solution:
    def solution_546_3(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(goal): return True
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]