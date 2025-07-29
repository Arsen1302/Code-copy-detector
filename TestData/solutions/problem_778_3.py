class Solution:
    def solution_778_3(self, s: str) -> str:
        return max(s[i:] for i in range(len(s)))