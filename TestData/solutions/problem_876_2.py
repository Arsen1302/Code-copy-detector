class Solution:
    def solution_876_2(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return ''
        for i in range(n//2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i+1:]
        return s[:-1] + 'b'