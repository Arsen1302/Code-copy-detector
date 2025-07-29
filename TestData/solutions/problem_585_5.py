class Solution:
    def solution_585_5(self, s: str, k: int) -> str:
        if k == 1:
            return min([s[i:] + s[:i] for i in range(len(s))])
        return ''.join(sorted(s))