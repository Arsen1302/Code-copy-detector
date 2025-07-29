class Solution:
    def solution_1090_3(self, s: str) -> int:
        ans = op = 0
        for c in s: 
            if c == "(": op += 1
            elif c == ")": op -= 1
            ans = max(ans, op)
        return ans