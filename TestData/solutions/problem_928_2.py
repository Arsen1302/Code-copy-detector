class Solution:
    def solution_928_2(self, s: str) -> str:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] == n:
                return s[i:]
            if i + z[i] > r:
                l, r = i, i + z[i]
        return ''