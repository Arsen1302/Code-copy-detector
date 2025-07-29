class Solution:
    def solution_101_5(self, s: str) -> str:
        if not s: return ""
        for i in reversed(range(len(s))):
            if s[0:i+1] == s[i::-1]:
                return s[:i:-1] + s