class Solution:
    def solution_198_5(self, s: str) -> int:
        ascii = [0] * 26

        for i in s:
            ascii[ord(i) - ord('a')] += 1

        for k, v in enumerate(s):
            if ascii[ord(v) - ord('a')] == 1:
                return k

        return -1