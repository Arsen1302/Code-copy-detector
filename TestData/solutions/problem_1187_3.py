class Solution:
    def solution_1187_3(self, s: str) -> int:
        lo, hi = 0, len(s)-1
        while lo < hi and s[lo] == s[hi]:
            ch = s[lo]
            while lo <= hi and s[lo] == ch: lo += 1
            while lo <= hi and s[hi] == ch: hi -= 1
        return hi - lo + 1