class Solution:
    def solution_320_1(self, s: str, k: int) -> str:
        if len(s)<(k):return s[::-1]
        if len(s)<(2*k):return (s[:k][::-1]+s[k:])
        return s[:k][::-1]+s[k:2*k]+self.solution_320_1(s[2*k:],k)