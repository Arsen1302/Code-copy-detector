class Solution:
    def solution_1672_2(self, s: str) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        start, max_len = 0, 0
        for i in range(1, len(s) + 1):  # from length 1 to len(s)
            if s[start:i] in alphabet:  # check whether slice is consecutive
                max_len = max(max_len, i - start)
            else:
                start = i - 1
        return max_len