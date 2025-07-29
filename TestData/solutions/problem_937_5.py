class Solution:
    def solution_937_5(self, s: str) -> int:
        ans = 0
        s = int(s,2)
        while s > 1:
            ans += 1
            s = s + 1 if s &amp; 1 else s >> 1

        return ans