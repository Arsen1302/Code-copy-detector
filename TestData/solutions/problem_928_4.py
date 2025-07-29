class Solution:
    def solution_928_4(self, s: str) -> str:
        a, m, p = 1103515245, 2**31, 1
        ans = -1
        prefix_hash, suffix_hash = 0, 0
        for i in range(len(s)-1):
            prefix_hash = (prefix_hash * a + ord(s[i])) % m
            suffix_hash = (suffix_hash + ord(s[-i-1]) * p) % m
            p = p * a % m
            if prefix_hash == suffix_hash and s[:i+1] == s[-i-1:]:
                ans = i
        return s[:ans+1]