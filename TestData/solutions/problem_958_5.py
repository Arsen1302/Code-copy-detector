class Solution:
    def solution_958_5(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        if s1 < s2:
            s1, s2 = s2, s1
        return all(c1 >= c2 for c1, c2 in zip(s1, s2))