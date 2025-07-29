class Solution:
    def solution_1272_4(self, s: str) -> bool:
        return len(max(s.split('0'),key=len)) > len(max(s.split('1'),key=len))