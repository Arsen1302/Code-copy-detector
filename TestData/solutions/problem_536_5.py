class Solution:
    def solution_536_5(self, s: str, shifts: List[int]) -> str:
        return (lambda offsets : "".join([chr(ord('a') + (offsets[i] + ord(s[i]) - ord('a')) % 26) for i in range(len(s))]))(list(accumulate(shifts[::-1]))[::-1])