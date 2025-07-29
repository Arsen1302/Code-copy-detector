class Solution:
    def solution_1579_2(self, s: str, target: str) -> int:
        cnt, cnt1 = Counter(s), Counter(target)
        return min(cnt[ch] // cnt1[ch] for ch in cnt1.keys())