class Solution:
    def solution_101_4(self, s: str) -> str:
        for i in range(len(s), -1, -1):
            if s[:i] == s[i-1::-1]:
                return s[:i-1:-1] + s