class Solution:
    def solution_1572_3(self, s: str, letter: str) -> int:
        cnt = 0
        for char in s:
            if char == letter:
                cnt += 1
        res = math.floor((cnt / len(s)) * 100)
        return res