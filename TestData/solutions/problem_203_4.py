class Solution:
    def solution_203_4(self, s: str, t: str) -> bool:
        i, j, m, n = 0, 0, len(s), len(t)
        while i < m and j < n and n - j >= m - i:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m