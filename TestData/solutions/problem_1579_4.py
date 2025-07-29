class Solution:
    def solution_1579_4(self, s: str, target: str) -> int:
        counter_s = Counter(s)
        res = float('inf')
        for k, v in Counter(target).items():
            res = min(res, counter_s[k] // v)
        return res