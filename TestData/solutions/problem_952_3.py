class Solution:
    def solution_952_3(self, s: str) -> int:
        s = list(s)
        res = 0
        a, b = 0, 0
        for i in range(1, len(s)):
            a = s[:i] # left side array
            b = s[i:] # right side array
            a = a.count('0') # count of 0 at left side
            b = b.count('1') # count of 1 at right side
            res = max(res, a + b)
        return  res