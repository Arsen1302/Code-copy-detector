class Solution:
    def solution_1116_4(self, s: str) -> int:
        ans = suffix = 0
        for c in reversed(s):
            if c == "a": suffix += 1
            else: ans = min(1 + ans, suffix)
        return ans