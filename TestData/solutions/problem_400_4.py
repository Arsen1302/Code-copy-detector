class Solution:
    def solution_400_4(self, s: str) -> bool:
        isPal = lambda s: s == s[::-1]
        if isPal(s): return True
        for i in range(len(s)):
            if isPal(s[:i] + s[i+1:]): return True
        return False