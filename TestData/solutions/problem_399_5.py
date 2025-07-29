class Solution:
    def solution_399_5(self, s: str) -> bool:
        counts = {0}
        for ch in s:
            if ch == "(":
                counts = set(prev+1 for prev in counts)
            elif ch == ")":
                counts = set(prev-1 for prev in counts if prev > 0)
            elif ch == "*":
                counts = set([prev+1 for prev in counts] + [prev-1 for prev in counts] + list(counts))
        return 0 in counts