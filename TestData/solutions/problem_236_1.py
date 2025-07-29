class Solution:
    def solution_236_1(self, s: str) -> int:
        return len([i for i in s.split(" ") if i!=""])