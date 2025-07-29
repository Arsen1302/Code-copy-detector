class Solution:
    def solution_1688_3(self, s: str) -> int:
        n = len(s)
        min_suffix, t, ans = [s[-1]] * n, [], []
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        for i, char in enumerate(s):
            t.append(char)
            while i + 1 < n and t and min_suffix[i + 1] >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return ''.join(ans)