class Solution:
    def solution_1624_3(self, s: str) -> str:
        mask = 0 
        for ch in s: 
            if mask &amp; 1<<ord(ch)-97: return ch 
            mask ^= 1<<ord(ch)-97