class Solution:
    def solution_981_5(self, s: str, k: int) -> bool:
        return len(set(s[i:i+k] for i in range(len(s)-k+1))) == 2**k