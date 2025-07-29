class Solution:
    def solution_600_5(self, s: str) -> str:
        s, left, right = list(s), 0, len(s) - 1
        while right >= left:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].isalpha():
                right -= 1
            elif s[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)