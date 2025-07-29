class Solution:
    def solution_1254_2(self, s: str) -> str:
        return ''.join(chr(ord(s[i-1]) + int(s[i])) if s[i].isdigit() else s[i] for i in range(len(s)))