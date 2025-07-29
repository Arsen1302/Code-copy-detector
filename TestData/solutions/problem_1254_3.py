class Solution:
    def solution_1254_3(self, s: str) -> str:
        answer = []
        for i, char in enumerate(s):
            if char.isdigit(): char = chr(ord(s[i-1]) + int(char))
            answer.append(char)
        return ''.join(answer)