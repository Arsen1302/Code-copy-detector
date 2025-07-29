class Solution:
    def solution_320_5(self, s: str, k: int) -> str:
        return ''.join(s[i:i+k][::-1] + s[i+k:i+k*2] for i in range(0, len(s), k*2))