class Solution:
    def solution_1303_3(self, s: str, part: str) -> str:
        l = len(part)
        while True:
            for i in range(len(s)-l+1):
                if s[i:i+l] == part:
                    s = s[:i] + s[i+l:]
                    break
            if part not in s:
                return s