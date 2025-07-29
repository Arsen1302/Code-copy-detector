class Solution:
    def solution_1572_4(self, s: str, letter: str) -> int:
        return int(s.count(letter)*100/len(s))