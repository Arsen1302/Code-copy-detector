class Solution:
    def solution_1327_2(self, s: str, k: int) -> int:
        s = "".join(str(ord(ch)-96) for ch in s)
        for _ in range(k): s = str(sum(int(ch) for ch in s))
        return int(s)