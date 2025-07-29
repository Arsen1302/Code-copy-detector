class Solution:
    def solution_1579_3(self, s: str, target: str) -> int:
        s = Counter(s)
        target = Counter(target)
        return min(s[c] // target[c] for c in target)