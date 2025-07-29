class Solution:
    def solution_1688_1(self, s: str) -> str:
        cnt, lo, p, t = Counter(s), 'a', [], []
        for ch in s:
            t += ch
            cnt[ch] -= 1
            while lo < 'z' and cnt[lo] == 0:
                lo = chr(ord(lo) + 1)
            while t and t[-1] <= lo:
                p += t.pop()
        return "".join(p)