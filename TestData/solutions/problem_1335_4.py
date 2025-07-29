class Solution:
    def solution_1335_4(self, s: str) -> str:
        t = ''
        ct = 1
        ans = ''
        for c in s:
            if c == t:
                ct += 1
            else:
                ct = 1
            if ct < 3:
                ans += c
            t = c
        return ans