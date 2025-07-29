class Solution:
    def solution_1231_4(self, C: str) -> bool:
        return (ord(C[0]) + ord(C[1])) &amp; 1