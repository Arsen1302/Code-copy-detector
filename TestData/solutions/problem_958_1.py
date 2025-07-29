class Solution:
    def solution_958_1(self, s1: str, s2: str) -> bool:
        return all(a<=b for a,b in zip(min(sorted(s1),sorted(s2)),max(sorted(s1),sorted(s2))))```