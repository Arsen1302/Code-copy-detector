class Solution:
    def solution_536_2(self, S: str, shifts: List[int]) -> str:
        return ''.join(chr((ord(letter) + shifting%26) - 26)  if (ord(letter) + shifting%26)>122 else chr((ord(letter) + shifting%26)) for letter,shifting in zip(S, list(accumulate(shifts[::-1]))[::-1]))