class Solution:
    def solution_981_1(self, s: str, k: int) -> bool:                
        return len({s[i:i+k] for i in range(len(s)-k+1)}) == 2 ** k