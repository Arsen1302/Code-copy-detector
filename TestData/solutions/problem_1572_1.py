class Solution:
    def solution_1572_1(self, s: str, letter: str) -> int:
        a = s.count(letter)
        return (a*100)//len(s)