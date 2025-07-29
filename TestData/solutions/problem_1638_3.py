class Solution:
    def solution_1638_3(self, s: str, k: int) -> int:
        lis = [0] * 26
        for ch in s:
            idx = ord(ch) - ord("a")
            mi, ma = max(0, idx - k), min(25, idx + k)
            last_lis = max(lis[mi: ma + 1])
            lis[idx] = last_lis + 1
        return max(lis)