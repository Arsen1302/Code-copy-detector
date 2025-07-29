class Solution:
    def solution_1468_5(self, s: str, k: int, fill: str) -> List[str]:
        groups = len(s)//k
        remaining = len(s)%k
        res = []
        for i in range(groups):
            res.append(s[i*k:i*k+k])
        if remaining > 0:
            res.append(s[len(s)-remaining:]+fill*(k-remaining))
        return res